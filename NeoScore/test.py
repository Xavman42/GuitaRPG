from neoscore.core import neoscore
from neoscore.core.units import Mm, ZERO
from neoscore.western.clef import Clef
from neoscore.western.clef_type import ClefType, KeySignatureLayout
from neoscore.western.staff import Staff

neoscore.setup()
POSITION = (Mm(0), Mm(0))
staff = Staff(POSITION, None, Mm(80))
_sharp_positions: KeySignatureLayout = {
    "f": (0, 0),
    "c": (1, 1.5),
    "g": (2, -0.5),
    "d": (3, 1),
    "a": (4, 2.5),
    "e": (5, 0.5),
    "b": (6, 2),
}
_flat_positions: KeySignatureLayout = {
    "b": (0, 2),
    "e": (1, 0.5),
    "a": (2, 2.5),
    "d": (3, 1),
    "g": (4, 3),
    "c": (5, 1.5),
    "f": (6, 3.5),
}
my_clef = ClefType('gClef8va', 3, 5, _sharp_positions, _flat_positions)
clef = Clef(ZERO, staff, my_clef)
neoscore.show(display_page_geometry=False)

