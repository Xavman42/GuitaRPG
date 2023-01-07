from map import *
from Plevel import *
from HUD import *
from multiprocessing import Process, Value


def refresh_func(func_time: float):
    global my_angle, my_move_dur, new_move, my_x_move_rate, my_y_move_rate, reference_time, rotate_dist, \
        my_next_point, my_staves, network, my_scene_changed, my_last_index, hud_last_index
    move_rate = 120
    if new_move:
        my_angle, distance, my_next_point, my_staves, my_scene_changed, my_last_index = \
            calculate_trajectory(my_point, my_last_point, my_last_index, possible_paths, my_staves, my_network,
                                 my_level_dict, my_xp_dict, my_network_points)
        my_move_dur = distance.base_value / move_rate
        my_x_move_rate = cos(radians(my_angle)) * move_rate
        my_y_move_rate = sin(radians(my_angle)) * move_rate
        a = my_angle
        b = my_prev_angle
        a, b = max(a, b), min(a, b)
        rotate_dist = min(a - b, b + 360 - a)
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
        new_move = False
        reference_time = time.time()
        hud_current_index.value = my_current_index
        hud_last_index.value = my_last_index
        neoscore.set_refresh_func(camera_rotate_refresh_func)


def camera_rotate_refresh_func(real_time: float) -> neoscore.RefreshFuncResult:
    global reference_time, my_prev_angle, my_scene_changed
    t = real_time - reference_time
    rotation_time = 1
    zoom = 5+5*(sin(t*pi/rotation_time))
    neoscore.set_viewport_scale(zoom)
    if abs(my_angle - my_prev_angle) < 180:
        neoscore.set_viewport_rotation(-my_prev_angle - t * (my_angle - my_prev_angle) / rotation_time)
    elif (my_angle-my_prev_angle) < 0:
        neoscore.set_viewport_rotation(-my_prev_angle + t * rotate_dist / rotation_time)
    else:
        neoscore.set_viewport_rotation(-my_prev_angle + t * rotate_dist / rotation_time)
    x, y = neoscore.get_viewport_center_pos()
    if t > rotation_time:
        neoscore.set_viewport_rotation(-my_prev_angle - (my_angle - my_prev_angle))
        reference_time = time.time()
        neoscore.set_refresh_func(camera_forward_refresh_func)
        my_prev_angle -= (my_prev_angle - my_angle)
    result = neoscore.RefreshFuncResult(my_scene_changed)
    my_scene_changed = False
    return result


def camera_forward_refresh_func(real_time: float) -> neoscore.RefreshFuncResult:
    global my_angle, my_move_dur, new_move, my_last_point, my_point, my_scene_changed
    t = real_time - reference_time
    x_offset = -4.9
    y_offset = 9.92
    x = Unit(my_network_points[my_point][0] + x_offset + t * my_x_move_rate)
    y = Unit(my_network_points[my_point][1] + y_offset + t * my_y_move_rate)
    neoscore.set_viewport_center_pos((x, y))
    x, y = neoscore.get_viewport_center_pos()
    if t > my_move_dur:
        my_last_point = my_point
        my_point = my_next_point
        new_move = True
        neoscore.set_refresh_func(refresh_func)
    result = neoscore.RefreshFuncResult(my_scene_changed)
    my_scene_changed = False
    return result


def hud_process_func(last_index, current_index):
    global ref_current_index
    def hud_refresh_func(func_time: float):
        global ref_current_index
        if ref_current_index != last_index.value:
            mini_staff[ref_current_index].pen = Pen("#000000", Unit(0.5))
            mini_staff[last_index.value].pen = Pen("#2a51ee", Unit(3))
            ref_current_index = last_index.value

        pass

    ref_current_index = 0
    neoscore.setup()
    initialize_map()
    my_network_points, possible_paths, my_network = make_network()
    mini_map_network = my_network
    mini_staff = []
    mini_scale = 9
    for coord in mini_map_network:
        mini_staff.append(Path.straight_line(Point(Unit(75+coord[0]/mini_scale), Unit(1+coord[1]/mini_scale)), None,
                                             Point(Unit(coord[2]/mini_scale-coord[0]/mini_scale),
                                                   Unit(coord[3]/mini_scale-coord[1]/mini_scale)), None,
                                             Brush.no_brush(), Pen("#000000", Unit(0.5))))
    mini_staff[0].pen = Pen("#2a51ee", Unit(3))
    hud_elements = []
    hud_elements, text_dict = make_level_text(hud_elements)
    x, y = neoscore.get_viewport_center_pos()
    hud_elements = set_hud_coordinates(hud_elements, x-Unit(125), y+Unit(75))

    neoscore.set_viewport_scale(5)
    neoscore.set_refresh_func(hud_refresh_func, 5)
    neoscore.show(display_page_geometry=False, auto_viewport_interaction_enabled=False,
                  min_window_size=(1920, 360), max_window_size=(1920, 360))


if __name__ == '__main__':
    hud_last_index = Value('i', 0)
    hud_current_index = Value('i', 0)
    hud_process = Process(target=hud_process_func, args=(hud_last_index, hud_current_index))
    hud_process.start()

    neoscore.setup()
    my_level_dict = make_cell_dict()
    my_level_dict = set_skill_probability(my_level_dict, "scrape", 1)
    my_xp_dict = make_xp_dict()

    initialize_map()
    my_network_points, possible_paths, my_network = make_network()

    scale = 4
    my_network_points = [[j * scale for j in i] for i in my_network_points]
    for i in range(4):
        my_network[:, i] *= scale
    my_staves = np.array([])
    for idx, coord in enumerate(my_network):
        my_staves = np.append(my_staves, make_map_segment(coord[0], coord[1], coord[2], coord[3]))

    my_point = 0
    my_current_index = 0
    my_next_point = 0
    my_prev_angle = 0
    my_angle = 0
    my_last_point = -1
    my_last_index = -1
    my_x_move_rate = 0
    my_y_move_rate = 0
    my_move_dur = 0
    rotate_dist = 0
    new_move = True
    my_scene_changed = False
    neoscore.set_viewport_center_pos((Unit(my_network_points[0][0] + 100), Unit(my_network_points[0][1])))
    neoscore.set_viewport_scale(5)
    reference_time = time.time()
    neoscore.show(refresh_func, display_page_geometry=False,
                  min_window_size=(1920, 680), max_window_size=(1920, 680))
