import numpy as np
from math import atan2, sin, cos, pi, sqrt, degrees, radians
from neoscore.common import *
import time
import random
from Plevel import *
from HUD import *


def make_map_segment(
        x_coordinate_start,
        y_coordinate_start,
        x_coordinate_end,
        y_coordinate_end):
    x_offset = -4.9
    y_offset = 9.92
    length = Unit(sqrt((x_coordinate_end - x_coordinate_start) ** 2 + (y_coordinate_end - y_coordinate_start) ** 2))
    rotation = degrees(atan2(y_coordinate_end - y_coordinate_start, x_coordinate_end - x_coordinate_start))
    x_coordinate = x_coordinate_start + x_offset
    y_coordinate = y_coordinate_start + y_offset
    length = length + Unit(sin(radians(rotation)) * y_offset) / 2
    length = length + Unit(cos(radians(rotation)) * x_offset)
    staff = Staff(
        pos=Point(Unit(x_coordinate), Unit(y_coordinate)),
        parent=None,
        length=length
    )
    staff.transform_origin = Point(Unit(x_offset), Unit(y_offset))
    staff.rotation = rotation
    return staff


def default_refresh_func(real_time: float):
    global my_angle, my_distance, my_move_dur, my_x_distance, my_y_distance, \
        my_x_move_rate, my_y_move_rate, reference_time, rotate_cw, rotate_dist
    t = real_time-start_time
    if new_move:
        my_angle, my_distance, my_x_distance, my_y_distance = calculate_trajectory()
        my_angle = my_angle
        my_move_dur = my_distance.base_value/move_rate
        my_x_move_rate = cos(radians(my_angle)) * move_rate
        my_y_move_rate = sin(radians(my_angle)) * move_rate
        a = my_angle
        b = prev_angle
        a, b = max(a, b), min(a, b)
        rotate_dist = min(a-b, b+360-a)
        if a > b:
            if a - b > b + 360 - a:
                rotate_dist = b + 360 - a  # positive
            else:
                rotate_dist = b - a  # negative
        else:
            if b - a > a + 360 - b:
                rotate_dist = a + 360 - b  # positive
            else:
                rotate_dist = a - b  # negative
        reference_time = time.time()
        neoscore.set_refresh_func(camera_rotate_refresh_func)


def calculate_trajectory():
    global new_move, next_point
    new_move = False
    path_options = []
    indices = []
    for index, point in enumerate(possible_paths):
        if point[0] == current_point:
            path_options.append(point[1])
            indices.append(index)
        if point[1] == current_point:
            path_options.append(point[0])
            indices.append(index)
    try:
        path_options.remove(last_point)
        indices.remove(last_point)
    except ValueError:
        pass
    try:
        path_options.remove(0)
    except ValueError:
        pass
    next_point = random.choice(path_options)
    my_index = indices[path_options.index(next_point)]
    my_region = possible_paths[my_index][2]
    populate_staff(current_point, next_point, my_region)
    angle = degrees(atan2(network_points[next_point][1]-network_points[current_point][1],
                          network_points[next_point][0]-network_points[current_point][0]))
    x_distance = Unit(network_points[next_point][0]-network_points[current_point][0])
    y_distance = Unit(network_points[next_point][1]-network_points[current_point][1])
    distance = Unit(sqrt((network_points[next_point][0]-network_points[current_point][0])**2 +
                         (network_points[next_point][1]-network_points[current_point][1])**2))
    get_path_arrows()
    return angle, distance, x_distance, y_distance


def get_path_arrows():
    path_options = []
    indices = []
    for index, point in enumerate(possible_paths):
        if point[0] == next_point:
            path_options.append(point[1])
            indices.append(index)
        if point[1] == next_point:
            path_options.append(point[0])
            indices.append(index)
    try:
        path_options.remove(last_point)
        indices.remove(last_point)
    except ValueError:
        pass
    try:
        path_options.remove(0)
    except ValueError:
        pass
    for path in path_options:
        angle = degrees(atan2(network_points[path][1] - network_points[current_point][1],
                        network_points[path][0] - network_points[current_point][0]))
        camera_x = neoscore.get_viewport_center_pos().x + Unit(100)
        camera_y = neoscore.get_viewport_center_pos().y - Unit(100)
        arrow_end_x = 30*Unit(cos(radians(angle)))
        arrow_end_y = 30*Unit(sin(radians(angle)))
        Path.arrow((camera_x, camera_y), None, (arrow_end_x, arrow_end_y), None)


def populate_staff(here, there, region):
    global last_index, staves, level_dict, xp_dict, text_dict, scene_changed
    try:
        staves[last_index].remove()
        staves[last_index] = make_map_segment(network[last_index][0], network[last_index][1], network[last_index][2],
                                              network[last_index][3])
    except ValueError:
        pass
    for index, i in enumerate(possible_paths):
        if (i[0] == here and i[1] == there) or (i[1] == here and i[0] == there):
            my_index = index
    InvisibleClef(Unit(0), staves[my_index], 'treble')
    # mini map highlighting
    mini_staff[last_index].pen = Pen()
    mini_staff[my_index].pen = Pen("#2a51ee", Unit(3))
    length = Unit(sqrt(
        (network[my_index][2] - network[my_index][0]) ** 2 + (network[my_index][3] - network[my_index][1]) ** 2))
    apply_region_modifier(level_dict, region, 10)
    xp_dict, level_dict = initialize_skill(xp_dict, level_dict, region)
    offset = Unit(100)
    cell_length = 0
    while Unit(offset) < length - Unit(100):
        func, reg = get_cell_func(level_dict)
        cell_length = func(staves[my_index], offset)
        xp_dict, lvl = increase_xp(xp_dict, reg)
        level_dict = set_skill_probability(level_dict, reg, lvl)
        text_dict[reg][0].text = reg + ": " + str(lvl)
        offset = offset + cell_length + Unit(30)
    last_index = my_index
    scene_changed = True


def camera_rotate_refresh_func(real_time: float) -> neoscore.RefreshFuncResult:
    global reference_time, prev_angle, hud_elements, scene_changed
    t = real_time - reference_time
    rotation_time = 1
    zoom = 5+5*(sin(t*pi/rotation_time))
    neoscore.set_viewport_scale(zoom)
    if abs(my_angle - prev_angle) < 180:
        neoscore.set_viewport_rotation(-prev_angle - t * (my_angle - prev_angle) / rotation_time)
    elif (my_angle-prev_angle) < 0:
        neoscore.set_viewport_rotation(-prev_angle + t * rotate_dist / rotation_time)
    else:
        neoscore.set_viewport_rotation(-prev_angle + t * rotate_dist / rotation_time)
    x, y = neoscore.get_viewport_center_pos()
    hud_elements = set_hud_coordinates(hud_elements, x, y)
    hud_elements = set_hud_rotation(hud_elements, neoscore.get_viewport_rotation(), x, y)
    if t > rotation_time:
        neoscore.set_viewport_rotation(-prev_angle - (my_angle - prev_angle))
        # neoscore.set_viewport_scale(4)
        # print(neoscore.get_viewport_scale())
        reference_time = time.time()
        neoscore.set_refresh_func(camera_forward_refresh_func)
        prev_angle -= (prev_angle - my_angle)
        prev_angle = prev_angle
    result = neoscore.RefreshFuncResult(scene_changed)
    scene_changed = False
    return result


def camera_forward_refresh_func(real_time: float) -> neoscore.RefreshFuncResult:
    global my_angle, my_distance, my_move_dur, new_move, last_point, current_point, hud_elements, scene_changed
    t = real_time - reference_time
    x_offset = -4.9
    y_offset = 9.92
    x = Unit(network_points[current_point][0] + x_offset + t * my_x_move_rate)
    y = Unit(network_points[current_point][1] + y_offset + t * my_y_move_rate)
    neoscore.set_viewport_center_pos((x, y))
    x, y = neoscore.get_viewport_center_pos()
    hud_elements = set_hud_coordinates(hud_elements, x, y)
    hud_elements = set_hud_rotation(hud_elements, neoscore.get_viewport_rotation(), x, y)
    if t > my_move_dur:
        last_point = current_point
        current_point = next_point
        new_move = True
        neoscore.set_refresh_func(default_refresh_func)
    result = neoscore.RefreshFuncResult(scene_changed)
    scene_changed = False
    return result


def make_level_text(my_hud_elements):
    scrape_text = Text((Unit(-50), Unit(-90)), None, "scrape: ", Font("Lora", 6))
    bartok_text = Text((Unit(-50), Unit(-80)), None, "Bartok: ", Font("Lora", 6))
    tambura_text = Text((Unit(-50), Unit(-70)), None, "tambura: ", Font("Lora", 6))
    perc_text = Text((Unit(-50), Unit(-60)), None, "perc: ", Font("Lora", 6))
    triad_text = Text((Unit(-10), Unit(-90)), None, "triads:", Font("Lora", 6))
    melody_text = Text((Unit(-10), Unit(-80)), None, "melody:", Font("Lora", 6))
    harmonic_text = Text((Unit(-10), Unit(-70)), None, "harmonics:", Font("Lora", 6))
    rake_text = Text((Unit(-10), Unit(-60)), None, "rake harm:", Font("Lora", 6))
    rasg_text = Text((Unit(40), Unit(-90)), None, "rasgueado:", Font("Lora", 6))
    tremolo_text = Text((Unit(40), Unit(-80)), None, "tremolo:", Font("Lora", 6))
    adv_harm_text = Text((Unit(40), Unit(-70)), None, "ext. harm:", Font("Lora", 6))
    my_hud_elements = add_element_to_hud(my_hud_elements, scrape_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, bartok_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, tambura_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, perc_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, triad_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, melody_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, harmonic_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, rake_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, rasg_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, tremolo_text)
    my_hud_elements = add_element_to_hud(my_hud_elements, adv_harm_text)
    level_texts = {'scrape': [scrape_text, 0],
                   'bartok': [bartok_text, 0],
                   'tambura': [tambura_text, 0],
                   'perc': [perc_text, 0],
                   'triad': [triad_text, 0],
                   'melody': [melody_text, 0],
                   'harmonic': [harmonic_text, 0],
                   'rake': [rake_text, 0],
                   'rasg': [rasg_text, 0],
                   'tremolo': [tremolo_text, 0],
                   'adv_harm': [adv_harm_text, 0]}
    return my_hud_elements, level_texts


def initialize_map():
    bound_val = 9999
    Path.rect((Mm(-bound_val), Mm(-bound_val)), None, Mm(2 * bound_val), Mm(2 * bound_val),
              Brush.no_brush(), "#ff00ff55")


def make_network():
    network_points = [
        # 0 scrape region
        [0, 0],  # start
        [200, 0],  # still scrape
        [250, -50],  # Bartok and tambura corner
        [250, 50],  # percussion
        [150, -50],  # Bartok
        # 5
        [150, -150],  # Bartok
        [250, -150],  # Bartok
        [290, -90],  # tambura
        [290, -10],  # tambura
        [330, -50],  # tambura
        # 10
        [350, 150],  # percussion
        [250, 250],  # percussion
        [150, 150],  # percussion
        [300, -175],  # rake harmonics
        [375, -250],  # rake harmonics
        # 15
        [375, -100],  # rake harmonics and natural harmonics
        [450, -175],  # rake harmonics
        [375, 0],  # natural harmonics
        [475, 0],  # natural harmonics
        [475, -100],  # natural harmonics
        # 20
        [425, 200],  # triads
        [425, 100],  # triads
        [550, 200],  # triads
        [550, 100],  # triads and melody
        [700, -50],  # melody
        # 25
        [650, -100],  # melody
        [500, 50],  # melody
        [750, 50],  # rasg
        [750, -150],  # rasg
        [800, -150],  # rasg
        # 30
        [800, 50],  # rasg and tremolo
        [900, 150],  # tremolo
        [700, 150],  # tremolo and adv harmony
        [800, 250],  # tremolo
        [600, 150],  # adv harmony
        # 35
        [600, 250],  # adv harmony
        [700, 250],  # adv harmony
        [1000, -150]  # ending
    ]
    possible_paths = [
        [0, 1, "scrape"],
        [1, 2, "none"],
        [1, 3, "none"],
        [2, 4, "bartok"],
        [4, 5, "bartok"],
        [5, 6, "bartok"],
        [2, 6, "bartok"],
        [2, 7, "tambura"],
        [2, 8, "tambura"],
        [7, 9, "tambura"],
        [8, 9, "tambura"],
        [3, 10, "perc"],
        [10, 11, "perc"],
        [11, 12, "perc"],
        [3, 12, "perc"],
        [6, 13, "none"],
        [9, 15, "none"],
        [10, 21, "none"],
        [13, 14, "rake"],
        [13, 15, "rake"],
        [14, 16, "rake"],
        [15, 16, "rake"],
        [15, 17, "harmonic"],
        [17, 18, "harmonic"],
        [18, 19, "harmonic"],
        [15, 19, "harmonic"],
        [20, 21, "triad"],
        [20, 22, "triad"],
        [21, 23, "triad"],
        [22, 23, "triad"],
        [23, 24, "melody"],
        [24, 25, "melody"],
        [23, 26, "melody"],
        [25, 26, "melody"],
        [17, 21, "none"],
        [18, 26, "none"],
        [16, 25, "none"],
        [16, 28, "none"],
        [24, 28, "none"],
        [22, 34, "none"],
        [27, 28, "rasg"],
        [28, 29, "rasg"],
        [29, 30, "rasg"],
        [27, 30, "rasg"],
        [30, 31, "tremolo"],
        [30, 32, "tremolo"],
        [32, 33, "tremolo"],
        [31, 33, "tremolo"],
        [32, 34, "adv_harm"],
        [34, 35, "adv_harm"],
        [35, 36, "adv_harm"],
        [32, 36, "adv_harm"],
        [27, 34, "none"],
        [29, 37, "none"]
    ]
    network = np.array([
        # scrape region
        # 0
        [network_points[0][0], network_points[0][1], network_points[1][0], network_points[1][1], 1, 1],
        # area 1 stitching
        [network_points[1][0], network_points[1][1], network_points[2][0], network_points[2][1], 1, 0],
        [network_points[1][0], network_points[1][1], network_points[3][0], network_points[3][1], 1, 0],
        # Bartok region
        [network_points[4][0], network_points[4][1], network_points[2][0], network_points[2][1], 1, 2],
        [network_points[4][0], network_points[4][1], network_points[5][0], network_points[5][1], 1, 2],
        # 5
        [network_points[5][0], network_points[5][1], network_points[6][0], network_points[6][1], 1, 2],
        [network_points[2][0], network_points[2][1], network_points[6][0], network_points[6][1], 1, 2],
        # tambura region
        [network_points[2][0], network_points[2][1], network_points[7][0], network_points[7][1], 1, 3],
        [network_points[2][0], network_points[2][1], network_points[8][0], network_points[8][1], 1, 3],
        [network_points[7][0], network_points[7][1], network_points[9][0], network_points[9][1], 1, 3],
        # 10
        [network_points[8][0], network_points[8][1], network_points[9][0], network_points[9][1], 1, 3],
        # percussion region
        [network_points[3][0], network_points[3][1], network_points[10][0], network_points[10][1], 1, 4],
        [network_points[10][0], network_points[10][1], network_points[11][0], network_points[11][1], 1, 4],
        [network_points[11][0], network_points[11][1], network_points[12][0], network_points[12][1], 1, 4],
        [network_points[12][0], network_points[12][1], network_points[3][0], network_points[3][1], 1, 4],
        # area 1-2 stitching
        # 15
        [network_points[6][0], network_points[6][1], network_points[13][0], network_points[13][1], 1, 0],
        [network_points[9][0], network_points[9][1], network_points[15][0], network_points[15][1], 1, 0],
        [network_points[10][0], network_points[10][1], network_points[21][0], network_points[21][1], 1, 0],
        # rake harmonics
        [network_points[13][0], network_points[13][1], network_points[14][0], network_points[14][1], 2, 5],
        [network_points[13][0], network_points[13][1], network_points[15][0], network_points[15][1], 2, 5],
        # 20
        [network_points[14][0], network_points[14][1], network_points[16][0], network_points[16][1], 2, 5],
        [network_points[15][0], network_points[15][1], network_points[16][0], network_points[16][1], 2, 5],
        # natural harmonics
        [network_points[17][0], network_points[17][1], network_points[15][0], network_points[15][1], 2, 6],
        [network_points[17][0], network_points[17][1], network_points[18][0], network_points[18][1], 2, 6],
        [network_points[18][0], network_points[18][1], network_points[19][0], network_points[19][1], 2, 6],
        # 25
        [network_points[15][0], network_points[15][1], network_points[19][0], network_points[19][1], 2, 6],
        # triads
        [network_points[20][0], network_points[20][1], network_points[21][0], network_points[21][1], 2, 7],
        [network_points[20][0], network_points[20][1], network_points[22][0], network_points[22][1], 2, 7],
        [network_points[22][0], network_points[22][1], network_points[23][0], network_points[23][1], 2, 7],
        [network_points[21][0], network_points[21][1], network_points[23][0], network_points[23][1], 2, 7],
        # melody
        # 30
        [network_points[23][0], network_points[23][1], network_points[24][0], network_points[24][1], 2, 8],
        [network_points[24][0], network_points[24][1], network_points[25][0], network_points[25][1], 2, 8],
        [network_points[23][0], network_points[23][1], network_points[26][0], network_points[26][1], 2, 8],
        [network_points[26][0], network_points[26][1], network_points[25][0], network_points[25][1], 2, 8],
        # area 2 stitching
        [network_points[17][0], network_points[17][1], network_points[21][0], network_points[21][1], 2, 0],
        # 30
        [network_points[18][0], network_points[18][1], network_points[26][0], network_points[26][1], 2, 0],
        [network_points[16][0], network_points[16][1], network_points[25][0], network_points[25][1], 2, 0],
        # area 2-3 stitching
        [network_points[16][0], network_points[16][1], network_points[28][0], network_points[28][1], 2, 0],
        [network_points[24][0], network_points[24][1], network_points[28][0], network_points[28][1], 2, 0],
        [network_points[22][0], network_points[22][1], network_points[34][0], network_points[34][1], 2, 0],
        # rasg
        # 35
        [network_points[27][0], network_points[27][1], network_points[28][0], network_points[28][1], 3, 9],
        [network_points[28][0], network_points[28][1], network_points[29][0], network_points[29][1], 3, 9],
        [network_points[30][0], network_points[30][1], network_points[29][0], network_points[29][1], 3, 9],
        [network_points[27][0], network_points[27][1], network_points[30][0], network_points[30][1], 3, 9],
        # tremolo
        [network_points[30][0], network_points[30][1], network_points[31][0], network_points[31][1], 3, 10],
        # 40
        [network_points[30][0], network_points[30][1], network_points[32][0], network_points[32][1], 3, 10],
        [network_points[32][0], network_points[32][1], network_points[33][0], network_points[33][1], 3, 10],
        [network_points[33][0], network_points[33][1], network_points[31][0], network_points[31][1], 3, 10],
        # adv harmony
        [network_points[34][0], network_points[34][1], network_points[32][0], network_points[32][1], 3, 11],
        [network_points[35][0], network_points[35][1], network_points[34][0], network_points[34][1], 3, 11],
        # 45
        [network_points[35][0], network_points[35][1], network_points[36][0], network_points[36][1], 3, 11],
        [network_points[36][0], network_points[36][1], network_points[32][0], network_points[32][1], 3, 11],
        # area 3 stitching
        [network_points[34][0], network_points[34][1], network_points[27][0], network_points[27][1], 3, 0],
        # ending
        [network_points[29][0], network_points[29][1], network_points[37][0], network_points[37][1], 3, 0]
    ])
    return network_points, possible_paths, network


if __name__ == '__main__':
    neoscore.setup()

    level_dict = make_cell_dict()
    level_dict = set_skill_probability(level_dict, "scrape", 1)
    xp_dict = make_xp_dict()

    last_point = -1
    last_index = -1
    current_point = 0
    next_point = 1
    move_rate = 20
    my_x_move_rate = 80
    my_y_move_rate = 0
    my_angle = 0
    my_distance = 0
    my_x_distance = 0
    my_y_distance = 0
    my_move_dur = 0
    new_move = True
    reference_time = 0
    prev_angle = 0
    rotate_cw = True
    rotate_dist = 0
    scene_changed = False

    initialize_map()
    x_off = -4.9
    y_off = 9.92
    network_points, possible_paths, network = make_network()
    mini_map_network = network
    mini_staff = []
    mini_scale = 9
    for coord in mini_map_network:
        mini_staff.append(Path.straight_line(Point(Unit(-175+coord[0]/mini_scale), Unit(-75+coord[1]/mini_scale)), None,
                                             Point(Unit(coord[2]/mini_scale-coord[0]/mini_scale),
                                                   Unit(coord[3]/mini_scale-coord[1]/mini_scale))))
    hud_elements = []
    for i in mini_staff:
        hud_elements = add_element_to_hud(hud_elements, i)
    hud_elements, text_dict = make_level_text(hud_elements)
    hud_elements = add_element_to_hud(hud_elements,
                                      Path.arrow((Unit(0), Unit(64)), None, (Unit(0), Unit(-5))))
    scale = 4
    network_points = [[j*scale for j in i] for i in network_points]
    network[:, 0] *= scale
    network[:, 1] *= scale
    network[:, 2] *= scale
    network[:, 3] *= scale
    staves = np.array([])

    for idx, coord in enumerate(network):
        staves = np.append(staves, make_map_segment(coord[0], coord[1], coord[2], coord[3]))
    start_time = time.time()
    neoscore.set_viewport_center_pos((Unit(network_points[last_point][0]+100), Unit(network_points[last_point][1])))
    neoscore.set_viewport_scale(5)
    neoscore.show(default_refresh_func, display_page_geometry=False,
                  min_window_size=(1920, 1080), max_window_size=(1920, 1080))

# This is what should actually be here
#     neoscore.setup()
#     level_dict = make_cell_dict()
#     level_dict = set_skill_probability(level_dict, "scrape", 1)
#     xp_dict = make_xp_dict()
#
#     initialize_map()
#     network_points, possible_paths, network = make_network()
#
#     scale = 4
#     network_points = [[j * scale for j in i] for i in network_points]
#     for i in range(4):
#         network[:, i] *= scale
#     staves = np.array([])
#     for idx, coord in enumerate(network):
#         staves = np.append(staves, make_map_segment(coord[0], coord[1], coord[2], coord[3]))
#
#     new_move = True
#     neoscore.set_viewport_center_pos((Unit(network_points[0][0] + 100), Unit(network_points[0][1])))
#     neoscore.set_viewport_scale(5)
#     reference_time = time.time()
#     neoscore.show(refresh_func, display_page_geometry=False,
#                   min_window_size=(1920, 1080), max_window_size=(1920, 1080))
