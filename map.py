import numpy as np
from neoscore.common import *

class map:
    
    def __init__(self, num_of_regions = 4):
        self.num_of_regions = num_of_regions
        self.region_coordinates_x = np.empty([0, 3], dtype=int)
        self.region_coordinates_y = np.empty([0, 3], dtype=int)
        self.generate_region_grid_coordinates()
        for i in range(self.num_of_regions):
            self.region_coordinates_x = np.append(self.region_coordinates_x,[self.generate_region_x()], axis=0)
            self.region_coordinates_y = np.append(self.region_coordinates_y,[self.generate_region_y()], axis=0)
                
    def generate_region_grid_coordinates(self):
        self.region_x = np.array([0, 100, 100, 100])
        self.region_y = np.array([100, 0, 100, 200])
        
    def generate_region_x(self):
        self.reg_x = np.array([20, 60, 40])
        return self.reg_x
        
    def generate_region_y(self):
        self.reg_y = np.array([20, 60, 40])
        return self.reg_y
    
    def calculate_length(self, pos_0_x, pos_1_x, pos_0_y, pos_1_y):
        return np.sqrt((pos_0_x - pos_1_x)**2 + (pos_0_y - pos_1_y)**2)
    
    def calculate_angle(self, pos_0_x, pos_1_x, pos_0_y, pos_1_y):
        return np.degrees(np.arctan((pos_0_y - pos_1_y)/(pos_0_x - pos_1_x)))

if __name__ == '__main__':
    neoscore.setup()

    my_map = map()
    print(my_map.region_coordinates_x)
    
    
    pos_0 = Point(0, 0)
    pos_1 = Point(500, 500)
    length = np.sqrt((pos_0.x - pos_1.x)**2 + (pos_0.y - pos_1.y)**2)
    angle = np.degrees(np.arctan((pos_0.y - pos_1.y)/(pos_0.x - pos_1.x)))
    print(length)
    print(angle)

    t = Text(Point(Unit(-9), Unit(13)), None, "o")

    #s = Staff(Point(Unit(0), Unit(0)), None, Unit(length))
    #s.rotation = -angle
    #s.transform_origin = Point(Unit(-9), Unit(13))

    pos_x = np.array([0, 500, 200, 654, 683, 185, 72])
    pos_y = np.array([0, 500, 500, 413, 15, 563, 478 ])

    for i in range(len(pos_x)):
        pos_x = np.append(pos_x, pos_x[0])
        pos_y = np.append(pos_y, pos_y[0])
        length = np.sqrt((pos_y[i] - pos_y[i+1])**2 + (pos_x[i] - pos_x[i+1])**2)
        if(pos_x[i] > pos_x[i+1]):
            length = -length
        #if(pos_y[i] > pos_y[i+1]):
        #    length = -length
        angle = np.degrees(np.arctan((pos_y[i] - pos_y[i+1])/(pos_x[i] - pos_x[i+1])))
        s = Staff(Point(Unit(pos_x[i]), -Unit(pos_y[i])), None, Unit(length))
        s.rotation = -angle
        print(s.rotation)
        
    neoscore.show(display_page_geometry=False)