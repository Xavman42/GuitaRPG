from math import sin, pi
from neoscore.common import *
import numpy as np


def refresh_func(t: float):
    global staves
    neoscore.set_viewport_rotation(t)
    for j in range(4):
        staves[j].remove()
        staves[j] = Staff(Point(Mm(0), Mm(20*j)), None, Mm(100))
        InvisibleClef(Unit(0), staves[j], 'treble')


neoscore.setup()
staves = np.array([])
for i in range(4):
    staves = np.append(staves, Staff(Point(Mm(0), Mm(20*i)), None, Mm(100)))

neoscore.show(refresh_func)
