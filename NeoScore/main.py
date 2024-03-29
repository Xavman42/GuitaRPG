import random

import pyOSC3
from neoscore.core.key_event import KeyEventType

from NeoScore.Particle import send_particle
from map import *
from Plevel import *
from HUD import *
from multiprocessing import Process, Value, Array, Manager
import os
import pathlib


def still_refresh_func(func_time: float):
    global my_scene_changed
    result = neoscore.RefreshFuncResult(my_scene_changed)
    my_scene_changed = False
    return result


def refresh_func(func_time: float):
    global my_angle, my_move_dur, new_move, my_x_move_rate, my_y_move_rate, reference_time, rotate_dist, \
        my_next_point, my_staves, network, my_scene_changed, my_last_index, hud_last_index, hud_share_dict, \
        my_top_layer_assets, my_density
    move_rate = 30
    if new_move:
        if not my_next_point == 37:
            my_density = max(my_density * 0.925, 0.2)
            my_angle, distance, my_next_point, my_staves, my_scene_changed, my_last_index, share_dict, indices, \
                path_options, my_current_point, my_region, region_text = \
                calculate_trajectory(my_point, my_last_point, my_last_index, possible_paths, my_staves, my_network,
                                     my_level_dict, my_xp_dict, my_network_points, hud_return_point.value, my_density)
            my_top_layer_assets = redo_top_layer_assets(my_top_layer_assets)
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
            # share_dict['current_region'] = my_region
            hud_region_text = {'1': region_text}
            hud_region_text_dict.update(hud_region_text)
            hud_share_dict.update(share_dict)
            hud_current_index.value = my_current_index
            hud_last_index.value = my_last_index
            hud_current_point.value = my_current_point
            hud_next_point.value = my_next_point
            try:
                send_particle(my_client, region_text, my_xp_dict[region_text][0])
            except KeyError:
                send_particle(my_client, "scrape", 1)
            neoscore.set_refresh_func(camera_rotate_refresh_func)
        else:
            end_text = Text((Unit(4030), Unit(-580)), None, "Congratulations!",
                            neoscore.default_font.modified(size=Unit(16)))
            send_particle(my_client, "end", 1)
            neoscore.set_refresh_func(still_refresh_func)


def camera_rotate_refresh_func(real_time: float) -> neoscore.RefreshFuncResult:
    global reference_time, my_prev_angle, my_scene_changed
    t = real_time - reference_time
    rotation_time = 1
    zoom = 5 + 5 * (sin(t * pi / rotation_time))
    neoscore.set_viewport_scale(zoom)
    if abs(my_angle - my_prev_angle) < 180:
        neoscore.set_viewport_rotation(-my_prev_angle - t * (my_angle - my_prev_angle) / rotation_time)
    elif (my_angle - my_prev_angle) < 0:
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


def direction_select(event):
    # Press key 'a' to cycle through path directions
    global direction_tick
    if event.event_type == KeyEventType.PRESS and event.text == 'a':
        direction_tick += 1


def start_game(event):
    # Press key 'a' to cycle through path directions
    if event.event_type == KeyEventType.PRESS:
        neoscore.set_refresh_func(refresh_func)
        start_text.remove()
        neoscore.set_key_event_handler(None)


def hud_process_func(last_index, current_index, share_dict, current_point, next_point, return_point, region_text_dict):
    global ref_current_index, arrows, direction_tick

    def still_hud_refresh_func(func_time: float):
        global my_scene_changed
        result = neoscore.RefreshFuncResult(my_scene_changed)
        my_scene_changed = False
        return result

    def hud_refresh_func(func_time: float):
        global ref_current_index, arrows, direction_tick
        path_options = []
        indices = []
        if ref_current_index != last_index.value:
            mini_staff[ref_current_index].pen = Pen("#000000", Unit(0.5))
            mini_staff[last_index.value].pen = Pen("#2a51ee", Unit(3))
            ref_current_index = last_index.value
            direction_tick = random.randint(0, 5)
        if not ref_current_index == 53:
            for index, point in enumerate(possible_paths):
                if point[0] == next_point.value:
                    path_options.append(point[1])
                    indices.append(index)
                if point[1] == next_point.value:
                    path_options.append(point[0])
                    indices.append(index)
            try:
                index = path_options.index(current_point.value)
                path_options.remove(current_point.value)
                indices.pop(index)
            except ValueError:
                pass
            try:
                index = path_options.index(0)
                path_options.remove(0)
                indices.pop(index)
            except ValueError:
                pass
        for i in arrows:
            i.remove()
        arrows = []
        if not ref_current_index == 53:
            for future_point in path_options:
                my_index = indices[path_options.index(future_point)]
                my_region = possible_paths[my_index][2]
                angle = degrees(atan2(network_points[future_point][1] - network_points[next_point.value][1],
                                      network_points[future_point][0] - network_points[next_point.value][0]))
                arrow_end_x = 30 * Unit(cos(radians(angle)))
                arrow_end_y = 30 * Unit(sin(radians(angle)))
                arrows.append(Path.arrow((Unit(0), Unit(0)), None, (arrow_end_x, arrow_end_y), None, Brush("#cccccc")))
            arrows[direction_tick % len(arrows)].brush = Brush("#2a51ee")
            return_point.value = path_options[direction_tick % len(arrows)]
            for key, value in share_dict.items():
                text_dict[key][0].text = str(key) + ": " + str(value)
            # text_dict['current_region'][0].text = str(region_text_dict.get('1'))

    ref_current_index = -1
    neoscore.setup()
    load_hud_assets()
    initialize_map()
    network_points, possible_paths, network = make_network()
    mini_map_network = network
    mini_staff = []
    mini_scale = 9
    direction_tick = 0
    for coord in mini_map_network:
        mini_staff.append(
            Path.straight_line(Point(Unit(72 + coord[0] / mini_scale), Unit(-1 + coord[1] / mini_scale)), None,
                               Point(Unit(coord[2] / mini_scale - coord[0] / mini_scale),
                                     Unit(coord[3] / mini_scale - coord[1] / mini_scale)), None,
                               Brush.no_brush(), Pen("#000000", Unit(0.5))))
    mini_staff[0].pen = Pen("#2a51ee", Unit(3))
    hud_elements = []
    arrows = []
    hud_elements, text_dict = make_level_text(hud_elements)
    x, y = neoscore.get_viewport_center_pos()
    hud_elements = set_hud_coordinates(hud_elements, x - Unit(125), y + Unit(75))

    neoscore.set_viewport_scale(5)
    neoscore.set_refresh_func(hud_refresh_func, 30)
    neoscore.set_key_event_handler(direction_select)
    neoscore.show(display_page_geometry=False, auto_viewport_interaction_enabled=False,
                  min_window_size=(1920, 360), max_window_size=(1920, 360))


def load_hud_assets():
    cwd = os.getcwd()
    rosette_segment = pathlib.Path(cwd + "/Assets/rosette_segment")
    western_red_cedar = pathlib.Path(cwd + "/Assets/western_red_cedar")
    Image((Unit(-192), Unit(-36)), None, western_red_cedar, scale = 1/5)
    Image((Unit(0), Unit(-36)), None, western_red_cedar, scale=1 / 5)
    for i in range(24):
        Image((Unit(-192+16.25*i), Unit(-36)), None, rosette_segment, scale = 1/64)
    for i in range(24):
        Image((Unit(-192+16.25*i), Unit(30)), None, rosette_segment, scale = 1/64)
    for i in range(5):
        temp = Image((Unit(-186), Unit(-36 + 16.25*i)), None, rosette_segment, scale = 1/64)
        temp.rotation = 90
    for i in range(5):
        temp = Image((Unit(191), Unit(-36 + 16.25*i)), None, rosette_segment, scale = 1/64)
        temp.rotation = 90


def arrange_background(asset, number, staff):
    for i in range(number):
        Image((Unit(i * 50 + random.randint(0, 20)), Unit(-125 - random.randint(0, 20))),
              staff, asset, scale=1 / 2)
    for i in range(number):
        temp = Image((Unit(120+i * 50 + random.randint(0, 20)), Unit(160 + random.randint(0, 20))),
                     staff, asset, scale=1 / 2)
        temp.rotation = 180


def load_assets():
    cwd = os.getcwd()
    disk = pathlib.Path(cwd + "/Assets/circle")

    # Image((Unit(100), Unit(-690)),
    #       None, pathlib.Path(cwd + "/Assets/Area_1"), scale=0.38)
    # Image((Unit(1145), Unit(-1070)),
    #       None, pathlib.Path(cwd + "/Assets/Area_2"), scale=0.38)
    # Image((Unit(2290), Unit(-700)),
    #       None, pathlib.Path(cwd + "/Assets/Area_3"), scale=0.38)

    top_layer_assets = []
    for i in my_network_points:
        top_layer_assets.append(Image((Unit((i[0]-42.5)), Unit((i[1]-12.5))), None, disk, scale=1/8))
    return top_layer_assets


def redo_top_layer_assets(top_layer_assets):
    cwd = os.getcwd()
    disk = pathlib.Path(cwd + "/Assets/circle")
    for i in top_layer_assets:
        i.remove()
    top_layer_assets = []
    for i in my_network_points:
        top_layer_assets.append(Image((Unit((i[0] - 42.5)), Unit((i[1] - 12.5))), None, disk, scale=1 / 8))
    return top_layer_assets


if __name__ == '__main__':
    manager = Manager()
    hud_share_dict = manager.dict()
    hud_region_text_dict = manager.dict()
    hud_last_index = Value('i', 0)
    hud_current_index = Value('i', 0)
    hud_current_point = Value('i', 0)
    hud_next_point = Value('i', 0)
    hud_return_point = Value('i', 1)
    hud_process = Process(target=hud_process_func, args=(hud_last_index, hud_current_index, hud_share_dict,
                                                         hud_current_point, hud_next_point,
                                                         hud_return_point, hud_region_text_dict))
    hud_process.start()

    neoscore.setup()
    my_client = pyOSC3.OSCClient()
    my_client.connect(('127.0.0.1', 57120))
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

    my_top_layer_assets = load_assets()
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
    neoscore.set_viewport_center_pos((Unit(my_network_points[0][0] - 10), Unit(my_network_points[0][1] + 10)))
    neoscore.set_viewport_scale(1)
    start_text = Text((Unit(-200), Unit(-200)), None, "Press any key to start", neoscore.default_font.modified(
        size=Unit(36)))
    neoscore.set_key_event_handler(start_game)
    reference_time = time.time()
    my_density = 2.0
    neoscore.show(still_refresh_func, display_page_geometry=False, auto_viewport_interaction_enabled=False,
                  min_window_size=(1920, 680), max_window_size=(1920, 680))
