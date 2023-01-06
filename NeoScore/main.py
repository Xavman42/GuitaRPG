from map import *
from Plevel import *
from HUD import *


def refresh_func(func_time: float):
    t = reference_time - func_time
    if new_move:
        return
        my_angle, my_distance, my_x_distance, my_y_distance = calculate_trajectory()


if __name__ == '__main__':
    neoscore.setup()
    level_dict = make_cell_dict()
    level_dict = set_skill_probability(level_dict, "scrape", 1)
    xp_dict = make_xp_dict()

    initialize_map()
    network_points, possible_paths, network = make_network()

    scale = 4
    network_points = [[j * scale for j in i] for i in network_points]
    for i in range(4):
        network[:, i] *= scale
    staves = np.array([])
    for idx, coord in enumerate(network):
        staves = np.append(staves, make_map_segment(coord[0], coord[1], coord[2], coord[3]))

    new_move = True
    neoscore.set_viewport_center_pos((Unit(network_points[0][0] + 100), Unit(network_points[0][1])))
    neoscore.set_viewport_scale(5)
    reference_time = time.time()
    neoscore.show(refresh_func, display_page_geometry=False,
                  min_window_size=(1920, 1080), max_window_size=(1920, 1080))
