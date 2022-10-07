import numpy as np
from neoscore.common import *

neoscore.setup()

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