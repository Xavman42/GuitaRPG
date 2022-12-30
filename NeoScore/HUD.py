from neoscore.common import *
import numpy as np
from math import sin, cos, radians


def add_element_to_hud(hud_list, element):
    hud_list.append([element, element.x, element.y])
    return hud_list


def set_hud_coordinates(hud_list, viewport_x, viewport_y):
    for item in hud_list:
        item[0].x = viewport_x + item[1]
        item[0].y = viewport_y + item[2]
    return hud_list


def set_hud_rotation(hud_list, rot, viewport_x, viewport_y):
    for item in hud_list:
        item[0].x = (item[1]) * cos(radians(rot)) + (item[2]) * sin(radians(rot))+viewport_x
        item[0].y = (item[2]) * cos(radians(rot)) - (item[1]) * sin(radians(rot))+viewport_y
        item[0].rotation = - rot
    return hud_list

    #self.obj.x = ((self.xpos_ini-x_point) * np.cos(t*np.deg2rad(degrees)/rot_time)-(self.ypos_ini-y_point)*np.sin(t*np.deg2rad(degrees)/rot_time))+x_point
    #self.obj.y = ((self.ypos_ini-y_point)*np.cos(t*np.deg2rad(degrees)/rot_time)+(self.xpos_ini-x_point)*np.sin(t*np.deg2rad(degrees)/rot_time))+y_point


def hud_refresh_func(t: float):
    global hud_elements
    x = 100*Unit(sin(t))+Unit(200)
    y = 100*Unit(sin(t))+Unit(200)
    neoscore.set_viewport_center_pos((x, y))
    x, y = neoscore.get_viewport_center_pos()
    hud_elements = set_hud_coordinates(hud_elements, x, y)
    neoscore.set_viewport_rotation(20*t)
    hud_elements = set_hud_rotation(hud_elements, neoscore.get_viewport_rotation(), x, y)


if __name__ == '__main__':
    neoscore.setup()

    bound_val = 9999
    Path.rect((Mm(-bound_val), Mm(-bound_val)), None, Mm(2 * bound_val), Mm(2 * bound_val),
              Brush.no_brush(), "#ff00ff55")
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
        [450, -175],   # rake harmonics
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
        #15
        [network_points[6][0], network_points[6][1], network_points[13][0], network_points[13][1], 1, 0],
        [network_points[9][0], network_points[9][1], network_points[15][0], network_points[15][1], 1, 0],
        [network_points[10][0], network_points[10][1], network_points[21][0], network_points[21][1], 1, 0],
        # rake harmonics
        [network_points[13][0], network_points[13][1], network_points[14][0], network_points[14][1], 2, 5],
        [network_points[13][0], network_points[13][1], network_points[15][0], network_points[15][1], 2, 5],
        #20
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
    mini_map_network = network
    mini_staff = []
    mini_scale = 9
    hud_elements = []
    for coord in mini_map_network:
        mini_staff.append(Path.straight_line(Point(Unit(100 + coord[0]/mini_scale), Unit(-100+coord[1]/mini_scale)), None,
                                             Point(Unit(coord[2]/mini_scale-coord[0]/mini_scale),
                                                   Unit(coord[3]/mini_scale-coord[1]/mini_scale))))
    for i in mini_staff:
        hud_elements = add_element_to_hud(hud_elements, i)
    neoscore.show(hud_refresh_func, min_window_size=(1280, 720),
                  max_window_size=(1280, 720))