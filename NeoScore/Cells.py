from neoscore.common import *
from neoscore.western.invisible_clef import InvisibleClef
import random


def scrape_rank_1(staff, x):
    start = Notehead(staff.unit(x), staff, "d", Duration(1, 4), table=notehead_tables.INVISIBLE)
    width = random.randint(3, 15)
    end = Notehead(staff.unit(x)+staff.unit(width), staff, "g'", Duration(1, 4), table=notehead_tables.INVISIBLE)
    RepeatingMusicTextLine((staff.unit(2), ZERO), start,
                           (staff.unit(0), ZERO), end,
                           "wiggleTrillFastest", None, None, None, "#919191")
    m1 = MusicText(
        (Unit(10), staff.unit(-5)),
        start,
        "guitarString6", None, "#919191"
    )
    m2 = MusicText(
        (Unit(30), staff.unit(0.2)),
        start,
        "guitarString6", None, "#919191"
    )
    m2.rotation = 180
    t1 = Text((staff.unit(x), staff.unit(-5)), staff, " ", neoscore.default_font.modified(italic=True))
    t2 = Text((staff.unit(x)+staff.unit(width), staff.unit(10)), staff, " ", neoscore.default_font.modified(italic=True))
    t2.rotation = 180
    length = Unit(staff.unit(width))
    return length


def scrape_rank_2(staff, x):
    start_1 = Notehead(staff.unit(x), staff, "d", Duration(1, 4), table=notehead_tables.INVISIBLE)
    width = random.randint(3, 7)
    end_1 = Notehead(staff.unit(x)+staff.unit(width), staff, "g'", Duration(1, 4), table=notehead_tables.INVISIBLE)
    RepeatingMusicTextLine((staff.unit(2), ZERO), start_1,
                           (staff.unit(0), ZERO), end_1,
                           "wiggleTrillFastest", None, None, None, "#919191")
    start_2 = Notehead(staff.unit(-2), end_1, "d", Duration(1, 4), table=notehead_tables.INVISIBLE)
    end_2 = Notehead(staff.unit(-2) + staff.unit(width), end_1, "g'", Duration(1, 4), table=notehead_tables.INVISIBLE)
    RepeatingMusicTextLine((staff.unit(2), ZERO), start_2,
                           (staff.unit(0), ZERO), end_2,
                           "wiggleTrillFastest", None, None, None, "#919191")
    m1 = MusicText(
        (Unit(0), staff.unit(-5)),
        start_1,
        "guitarString6", None, "#919191"
    )
    m2 = MusicText(
        (Unit(0), staff.unit(5)),
        end_2,
        "guitarString6", None, "#919191"
    )
    m2.rotation = 180
    t1 = Text((staff.unit(x), staff.unit(-5)), staff, " ", neoscore.default_font.modified(italic=True))
    t2 = Text((staff.unit(x)+staff.unit(8), staff.unit(10)), staff, " ", neoscore.default_font.modified(italic=True))
    t2.rotation = 180
    length = 2.1 * staff.unit(width)
    return length


def scrape_rank_3(staff, x):
    p1 = Notehead(staff.unit(x), staff, "d", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p2 = Notehead(staff.unit(x)+staff.unit(2), staff, "a", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p3 = Notehead(staff.unit(x)+staff.unit(3), staff, "e", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p4 = Notehead(staff.unit(x)+staff.unit(4), staff, "d'", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p5 = Notehead(staff.unit(x)+staff.unit(5), staff, "a", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p6 = Notehead(staff.unit(x)+staff.unit(6), staff, "g'", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p7 = Notehead(staff.unit(x)+staff.unit(7), staff, "d'", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p8 = Notehead(staff.unit(x)+staff.unit(9), staff, "a'", Duration(1, 4), table=notehead_tables.INVISIBLE)
    RepeatingMusicTextLine((staff.unit(1), ZERO), p1,
                           (staff.unit(1), ZERO), p2,
                           "wiggleTrillFastest", None, None, None, "#919191")
    RepeatingMusicTextLine((staff.unit(0), ZERO), p2,
                           (staff.unit(0), ZERO), p3,
                           "wiggleTrillFastest", None, None, None, "#919191")
    RepeatingMusicTextLine((staff.unit(1), ZERO), p3,
                           (staff.unit(1), ZERO), p4,
                           "wiggleTrillFastest", None, None, None, "#919191")
    RepeatingMusicTextLine((staff.unit(0), ZERO), p4,
                           (staff.unit(0), ZERO), p5,
                           "wiggleTrillFastest", None, None, None, "#919191")
    RepeatingMusicTextLine((staff.unit(1), ZERO), p5,
                           (staff.unit(1), ZERO), p6,
                           "wiggleTrillFastest", None, None, None, "#919191")
    RepeatingMusicTextLine((staff.unit(0), ZERO), p6,
                           (staff.unit(0), ZERO), p7,
                           "wiggleTrillFastest", None, None, None, "#919191")
    RepeatingMusicTextLine((staff.unit(1), ZERO), p7,
                           (staff.unit(1), ZERO), p8,
                           "wiggleTrillFastest", None, None, None, "#919191")
    m1 = MusicText(
        (Unit(-4), staff.unit(-6)),
        p1,
        "guitarString6", None, "#919191"
    )
    m2 = MusicText(
        (Unit(8), staff.unit(6)),
        p8,
        "guitarString6", None, "#919191"
    )
    m2.rotation = 180
    t1 = Text((staff.unit(x), staff.unit(-5)), staff, " ", neoscore.default_font.modified(italic=True))
    t2 = Text((staff.unit(x)+staff.unit(10), staff.unit(10)), staff, " ", neoscore.default_font.modified(italic=True))
    t2.rotation = 180
    length = Unit(staff.unit(10))
    return length


def scrape_rank_4(staff, x):
    p1 = Notehead(staff.unit(x), staff, "d", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p2 = Notehead(staff.unit(x)+staff.unit(2), staff, "f'", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p3 = Notehead(staff.unit(x)+staff.unit(4), staff, "d", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p4 = Notehead(staff.unit(x)+staff.unit(6), staff, "f'", Duration(1, 4), table=notehead_tables.INVISIBLE)
    p5 = Notehead(staff.unit(x)+staff.unit(8), staff, "d", Duration(1, 4), table=notehead_tables.INVISIBLE)
    RepeatingMusicTextLine((staff.unit(1), ZERO), p1,
                           (staff.unit(1), ZERO), p2,
                           "wiggleTrillFastest", None, None, None, "#919191")
    RepeatingMusicTextLine((staff.unit(0), ZERO), p2,
                           (staff.unit(0), ZERO), p3,
                           "wiggleTrillFastest", None, None, None, "#919191")
    RepeatingMusicTextLine((staff.unit(1), ZERO), p3,
                           (staff.unit(1), ZERO), p4,
                           "wiggleTrillFastest", None, None, None, "#919191")
    RepeatingMusicTextLine((staff.unit(0), ZERO), p4,
                           (staff.unit(0), ZERO), p5,
                           "wiggleTrillFastest", None, None, None, "#919191")
    m1 = MusicText(
        (Unit(-6), staff.unit(-6)),
        p1,
        "guitarString6", None, "#919191"
    )
    m2 = MusicText(
        (Unit(10), staff.unit(1)),
        p5,
        "guitarString6", None, "#919191"
    )
    m2.rotation = 180
    t1 = Text((staff.unit(x), staff.unit(-5)), staff, " ", neoscore.default_font.modified(italic=True))
    t2 = Text((staff.unit(x)+staff.unit(10), staff.unit(10)), staff, " ", neoscore.default_font.modified(italic=True))
    t2.rotation = 180
    length = Unit(staff.unit(10))
    return length


def bartok_rank_1(staff, x):
    p1 = Chordrest(staff.unit(x)+staff.unit(0.5), staff, ["a,"], Duration(1, 4))
    for n in p1.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(2.2)),
        p1.highest_notehead,
        "pluckedSnapPizzicatoAbove", None, "#e63b07"
    )
    p2 = Chordrest(staff.unit(x), staff, ["c''"], Duration(1, 4))
    for n in p2.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(-1.5)),
        p2.highest_notehead,
        "pluckedSnapPizzicatoBelow", None, "#e63b07"
    )
    m1 = MusicText(
        (Unit(-8), staff.unit(11)),
        p1,
        "guitarString5", None, "#e63b07"
    )
    m2 = MusicText(
        (Unit(8), staff.unit(-7.5)),
        p2,
        "guitarString5", None, "#e63b07"
    )
    m2.rotation = 180
    length = Unit(staff.unit(2))
    return length


def bartok_rank_2(staff, x):
    p1 = Chordrest(staff.unit(x)+staff.unit(0.5), staff,
                   [random.choice(["e", "d", "c", "b,", "a,", "g,", "f,"])], Duration(1, 4))
    for n in p1.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(2.2)),
        p1.highest_notehead,
        "pluckedSnapPizzicatoAbove", None, "#e63b07"
    )
    p2 = Chordrest(staff.unit(x), staff, ["f''"], Duration(1, 4))
    for n in p2.noteheads:
        n.brush = "#e63b07"
    p3 = Chordrest(staff.unit(x)+staff.unit(5.5), staff, ["e,"], Duration(1, 4))
    for n in p3.noteheads:
        n.brush = "#e63b07"
    p4 = Chordrest(staff.unit(x)+staff.unit(5), staff,
                   [random.choice(["f'", "g'", "a'", "b'", "c''", "d''", "e''"])], Duration(1, 4))
    for n in p4.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(-1.5)),
        p4.highest_notehead,
        "pluckedSnapPizzicatoBelow", None, "#e63b07"
    )
    m1 = MusicText(
        (Unit(-8), staff.unit(11)),
        p1,
        "guitarString6", None, "#e63b07"
    )
    m2 = MusicText(
        (Unit(8), staff.unit(-7.5)),
        p3,
        "guitarString6", None, "#e63b07"
    )
    m2.rotation = 180
    Slur((staff.unit(1), staff.unit(1)), p1.lowest_notehead,
         (staff.unit(-2), staff.unit(8)), p3, direction=DirectionY.DOWN, brush="#e63b07")
    Slur((staff.unit(0), staff.unit(-1)), p4.lowest_notehead,
         (staff.unit(1), staff.unit(-5)), p2, direction=DirectionY.UP, brush="#e63b07")
    length = Unit(staff.unit(7))
    return length


def bartok_rank_3(staff, x):
    p1 = Chordrest(staff.unit(x)+staff.unit(0.5), staff, [random.choice(["a", "g", "f", "e", "d", "c", "b,"])],
                   Duration(1, 4))
    for n in p1.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(2.2)),
        p1.highest_notehead,
        "pluckedSnapPizzicatoAbove", None, "#e63b07"
    )
    p2 = Chordrest(staff.unit(x), staff, ["c''"], Duration(1, 4))
    for n in p2.noteheads:
        n.brush = "#e63b07"
    p3 = Chordrest(staff.unit(x)+staff.unit(5.5), staff, ["a,"], Duration(1, 4))
    for n in p3.noteheads:
        n.brush = "#e63b07"
    p4 = Chordrest(staff.unit(x)+staff.unit(5), staff, [random.choice(["c'", "d'", "e'", "f'", "g'", "a'", "b'"])],
                   Duration(1, 4))
    for n in p4.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(-1.5)),
        p4.highest_notehead,
        "pluckedSnapPizzicatoBelow", None, "#e63b07"
    )
    m1 = MusicText(
        (Unit(-8), staff.unit(10)),
        p1,
        "guitarString5", None, "#e63b07"
    )
    m2 = MusicText(
        (Unit(8), staff.unit(-7.5)),
        p3,
        "guitarString5", None, "#e63b07"
    )
    m2.rotation = 180
    Slur((staff.unit(1), staff.unit(1)), p1.lowest_notehead,
         (staff.unit(-2), staff.unit(6)), p3, direction=DirectionY.DOWN, brush="#e63b07")
    Slur((staff.unit(0), staff.unit(-1)), p4.lowest_notehead,
         (staff.unit(1), staff.unit(-3)), p2, direction=DirectionY.UP, brush="#e63b07")
    length = Unit(staff.unit(7))
    return length


def bartok_rank_4(staff, x):
    p1 = Chordrest(staff.unit(x)+staff.unit(0.5), staff, [random.choice(["b,", "c", "d"])], Duration(1, 4))
    for n in p1.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(2.2)),
        p1.highest_notehead,
        "pluckedSnapPizzicatoAbove", None, "#e63b07"
    )
    p2 = Chordrest(staff.unit(x), staff, [random.choice(["b'", "a'", "g'"])], Duration(1, 4))
    for n in p2.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(-1.5)),
        p2.highest_notehead,
        "pluckedSnapPizzicatoBelow", None, "#e63b07"
    )
    p3 = Chordrest(staff.unit(x)+staff.unit(4.5), staff, [random.choice(["g,", "a,", "b,", "c"])], Duration(1, 4))
    for n in p3.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(2.2)),
        p3.highest_notehead,
        "pluckedSnapPizzicatoAbove", None, "#e63b07"
    )
    p4 = Chordrest(staff.unit(x)+staff.unit(4), staff, [random.choice(["d''", "c''", "b'", "a'"])], Duration(1, 4))
    for n in p4.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(-1.5)),
        p4.highest_notehead,
        "pluckedSnapPizzicatoBelow", None, "#e63b07"
    )
    p5 = Chordrest(staff.unit(x)+staff.unit(8.5), staff, [random.choice(["e", "f", "g"])],
                   Duration(1, 4), stem_direction=DirectionY.DOWN)
    for n in p5.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(5)),
        p5.highest_notehead,
        "pluckedSnapPizzicatoAbove", None, "#e63b07"
    )
    p6 = Chordrest(staff.unit(x)+staff.unit(8), staff, [random.choice(["f'", "e'", "d'"])],
                   Duration(1, 4), stem_direction=DirectionY.UP)
    for n in p6.noteheads:
        n.brush = "#e63b07"
    MusicText(
        (Unit(1), staff.unit(-4)),
        p6.highest_notehead,
        "pluckedSnapPizzicatoBelow", None, "#e63b07"
    )
    m1 = MusicText(
        (Unit(-8), staff.unit(11)),
        p1,
        "guitarString5", None, "#e63b07"
    )
    m2 = MusicText(
        (Unit(8), staff.unit(-7.5)),
        p2,
        "guitarString5", None, "#e63b07"
    )
    m2.rotation = 180
    m3 = MusicText(
        (Unit(-8), staff.unit(11)),
        p3,
        "guitarString6", None, "#e63b07"
    )
    m4 = MusicText(
        (Unit(8), staff.unit(-7.5)),
        p4,
        "guitarString6", None, "#e63b07"
    )
    m4.rotation = 180
    m5 = MusicText(
        (Unit(-8), staff.unit(11)),
        p5,
        "guitarString4", None, "#e63b07"
    )
    m6 = MusicText(
        (Unit(8), staff.unit(-7.5)),
        p6,
        "guitarString4", None, "#e63b07"
    )
    m6.rotation = 180
    length = Unit(staff.unit(13))
    return length


def tambura_rank_1(staff, x):
    r1 = Path.rect((staff.unit(x), staff.unit(-2)), staff, Unit(10), Unit(40), "#2e2afa50")
    t1 = Text((staff.unit(-3), staff.unit(-4)), r1, "tambura", neoscore.default_font.modified(italic=True), "#2e2afa")
    c1 = Text((staff.unit(-0.5), staff.unit(-1)), r1, random.choice(["G5", "A5", "B5", "C5"]), None, "#2e2afa")
    t2 = Text((staff.unit(5.5), staff.unit(12.5)), r1, "tambura", neoscore.default_font.modified(italic=True),
              "#2e2afa")
    c2 = Text((staff.unit(3), staff.unit(10)), r1, random.choice(["G5", "A5", "B5", "C5"]), None, "#2e2afa")
    t2.rotation = 180
    c2.rotation = 180
    length = Unit(staff.unit(6))
    return length


def tambura_rank_2(staff, x):
    r1 = Path.rect((staff.unit(x), staff.unit(-2)), staff, Unit(10), Unit(40), "#2e2afa50")
    t1 = Text((staff.unit(-3), staff.unit(-4)), r1, "tambura", neoscore.default_font.modified(italic=True), "#2e2afa")
    # While there is a SMuFL for guitar barre C, it's so similar to a text C that I don't think I'll bother
#    c1 = MusicText(
#        (staff.unit(x - 3.5), staff.unit(-1)),
#        r1,
#        "guitarBarreFull",
#    )
    c1 = Text((staff.unit(-0.5), staff.unit(-1)), r1,
              "C" + random.choice(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]),
              neoscore.default_font.modified(weight=80), "#2e2afa")
    t2 = Text((staff.unit(5.5), staff.unit(12.5)), r1, "tambura", neoscore.default_font.modified(italic=True),
              "#2e2afa")
    c2 = Text((staff.unit(3), staff.unit(10)), r1,
              "C" + random.choice(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]),
              neoscore.default_font.modified(weight=80), "#2e2afa")
    t2.rotation = 180
    c2.rotation = 180
    length = Unit(staff.unit(7))
    return length


def tambura_rank_3(staff, x):
    chord_1 = random.choice(["G5", "A5", "B5", "C5"])
    chord_2 = random.choice(["G5", "A5", "B5", "C5"])
    chord_3 = random.choice(["G5", "A5", "B5", "C5"])
    r1 = Path.rect((staff.unit(x), staff.unit(-2)), staff, Unit(10), Unit(40), "#2e2afa50")
    t1 = Text((staff.unit(-3), staff.unit(-4)), r1, "tambura", neoscore.default_font.modified(italic=True), "#2e2afa")
    c1 = Text((staff.unit(-0.5), staff.unit(-1)), r1, chord_1, None, "#2e2afa")
    c2 = Text((staff.unit(2.5), staff.unit(10)), r1, chord_1, None, "#2e2afa")
    c2.rotation = 180
    r2 = Path.rect((staff.unit(x)+staff.unit(4), staff.unit(-2)), staff, Unit(10), Unit(40), "#2e2afa50")
    c3 = Text((staff.unit(-0.5), staff.unit(-1)), r2, chord_1, None, "#2e2afa")
    c4 = Text((staff.unit(2.5), staff.unit(10)), r2, chord_1, None, "#2e2afa")
    c4.rotation = 180
    r3 = Path.rect((staff.unit(x)+staff.unit(10), staff.unit(-2)), staff, Unit(10), Unit(40), "#2e2afa50")
    c5 = Text((staff.unit(-0.5), staff.unit(-1)), r3, chord_2, None, "#2e2afa")
    c6 = Text((staff.unit(2.5), staff.unit(10)), r3, chord_2, None, "#2e2afa")
    c6.rotation = 180
    r4 = Path.rect((staff.unit(x)+staff.unit(16), staff.unit(-2)), staff, Unit(10), Unit(40), "#2e2afa50")
    c7 = Text((staff.unit(-0.5), staff.unit(-1)), r4, chord_3, None, "#2e2afa")
    c8 = Text((staff.unit(2.5), staff.unit(10)), r4, chord_3, None, "#2e2afa")
    c8.rotation = 180
    t2 = Text((staff.unit(5.5), staff.unit(12.5)), r4, "tambura", neoscore.default_font.modified(italic=True),
              "#2e2afa")
    t2.rotation = 180
    length = Unit(staff.unit(18))
    return length


def tambura_rank_4(staff, x):
    chord = "C" + random.choice(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"])
    for i in range(6):
        r1 = Path.rect((staff.unit(x)+staff.unit(3*i), staff.unit(-2)), staff, Unit(10), Unit(40), "#2e2afa50")
    c1 = Text((staff.unit(-15.5), staff.unit(-1)), r1, chord, neoscore.default_font.modified(weight=80), "#2e2afa")
    c2 = Text((staff.unit(3), staff.unit(10)), r1, chord, neoscore.default_font.modified(weight=80), "#2e2afa")
    c2.rotation = 180
    t1 = Text((staff.unit(-17), staff.unit(-4)), r1, "tambura", neoscore.default_font.modified(italic=True), "#2e2afa")
    t2 = Text((staff.unit(5.5), staff.unit(12.5)), r1, "tambura", neoscore.default_font.modified(italic=True),
              "#2e2afa")
    t2.rotation = 180
    length = Unit(staff.unit(17))
    return length


def perc_rank_1(staff, x):
    r1 = Path.rect((staff.unit(x), staff.unit(-2)), staff, Unit(4), Unit(40), "#f2bb0580")
    t1 = Text((staff.unit(-2), staff.unit(-2)), r1, " ", neoscore.default_font.modified(italic=True), "#f2bb05")
    t2 = Text((staff.unit(2.5), staff.unit(10)), r1, " ", neoscore.default_font.modified(italic=True), "#f2bb05")
    t2.rotation = 180
    length = Unit(staff.unit(3))
    return length


def perc_rank_2(staff, x):
    t1 = Text((staff.unit(x), staff.unit(-2)), staff, " ", neoscore.default_font.modified(italic=True), "#f2bb05")
    n1 = Notehead(staff.unit(1), t1, "g'", Duration(1, 4), table=notehead_tables.X)
    n1.brush = "#f2bb05"
    n2 = Notehead(staff.unit(1), n1, "e'", Duration(1, 4), table=notehead_tables.X)
    n2.brush = "#f2bb05"
    n3 = Notehead(staff.unit(1), n2, "f'", Duration(1, 4), table=notehead_tables.X)
    n3.brush = "#f2bb05"
    n4 = Notehead(staff.unit(1), n3, "d'", Duration(1, 4), table=notehead_tables.X)
    n4.brush = "#f2bb05"
    n5 = Notehead(staff.unit(1), n4, "e'", Duration(1, 4), table=notehead_tables.X)
    n5.brush = "#f2bb05"
    n6 = Notehead(staff.unit(1), n5, "b", Duration(1, 4), table=notehead_tables.X)
    n6.brush = "#f2bb05"
    n7 = Notehead(staff.unit(1), n6, "c'", Duration(1, 4), table=notehead_tables.X)
    n7.brush = "#f2bb05"
    n8 = Notehead(staff.unit(1), n7, "a", Duration(1, 4), table=notehead_tables.X)
    n8.brush = "#f2bb05"
    n9 = Notehead(staff.unit(1), n8, "b", Duration(1, 4), table=notehead_tables.X)
    n9.brush = "#f2bb05"
    n10 = Notehead(staff.unit(1), n9, "g", Duration(1, 4), table=notehead_tables.X)
    n10.brush = "#f2bb05"
    n11 = Notehead(staff.unit(1), n10, "a", Duration(1, 4), table=notehead_tables.X)
    n11.brush = "#f2bb05"
    n12 = Notehead(staff.unit(1), n11, "f", Duration(1, 4), table=notehead_tables.X)
    n12.brush = "#f2bb05"
    n13 = Notehead(staff.unit(1), n12, "g", Duration(1, 4), table=notehead_tables.X)
    n13.brush = "#f2bb05"
    n14 = Notehead(staff.unit(1), n13, "e", Duration(1, 4), table=notehead_tables.X)
    n14.brush = "#f2bb05"
    n15 = Notehead(staff.unit(1), n14, "f", Duration(1, 4), table=notehead_tables.X)
    n15.brush = "#f2bb05"
    n16 = Notehead(staff.unit(1), n15, "d", Duration(1, 4), table=notehead_tables.X)
    n16.brush = "#f2bb05"
    t2 = Text((staff.unit(0), staff.unit(2)), n16, " ", neoscore.default_font.modified(italic=True), "#f2bb05")
    t2.rotation = 180
    length = Unit(staff.unit(18))
    return length


def perc_rank_3(staff, x):
    r1 = Path.ellipse((staff.unit(x), staff.unit(-2)), staff, Unit(8), Unit(20), "#f2bb0580")
    r2 = Path.ellipse((staff.unit(6), staff.unit(2)), r1, Unit(8), Unit(20), "#f2bb0580")
    r3 = Path.ellipse((staff.unit(3), staff.unit(2)), r2, Unit(8), Unit(20), "#f2bb0580")
    r4 = Path.ellipse((staff.unit(2), staff.unit(-4)), r3, Unit(8), Unit(20), "#f2bb0580")
    t1 = Text((staff.unit(-2), staff.unit(-2)), r1, " ", neoscore.default_font.modified(italic=True), "#f2bb0580")
    t2 = Text((staff.unit(13.5), staff.unit(10)), r1, " ", neoscore.default_font.modified(italic=True), "#f2bb0580")
    t2.rotation = 180
    length = Unit(staff.unit(14))
    return length


def perc_rank_4(staff, x):
    t1 = Text((staff.unit(x), staff.unit(-2)), staff, " ", neoscore.default_font.modified(italic=True), "#f2bb05")
    for i in range(40):
        Path.ellipse((Unit(random.randint(0, 60)), Unit(random.randint(0, 40))), t1, Unit(2), Unit(2), "#f2bb05200")
    t2 = Text((staff.unit(13.5), staff.unit(10)), t1, " ", neoscore.default_font.modified(italic=True), "#f2bb05")
    t2.rotation = 180
    length = Unit(staff.unit(14))
    return length


def triad_rank_1(staff, x):
    c1 = Chordrest(staff.unit(x), staff, ["g", "b", "d'"], (1, 1))
    for n in c1.noteheads:
        n.brush = "#10ada0"
    box = Path.rect((staff.unit(-0.5), staff.unit(-1)), c1, staff.unit(2.75), staff.unit(6), brush=Brush.no_brush())
    dur = random.randint(2, 9)
    arrow1 = Path.arrow((staff.unit(2.5), staff.unit(2)), c1,
                        (staff.unit(dur), staff.unit(0)), brush="#10ada080", pen=Pen("#10ada080", Mm(1)))
    arrow2 = Path.arrow((staff.unit(-0.75), staff.unit(2)), c1,
                        (staff.unit(-dur), staff.unit(0)), brush="#10ada080", pen=Pen("#10ada080", Mm(1)))
    length = Unit(staff.unit(3+2*dur))
    return length


def triad_rank_2(staff, x):
    c1 = Chordrest(staff.unit(x), staff, ["f", "a", "c'"], (1, 1))
    for n in c1.noteheads:
        n.brush = "#10ada0"
    box = Path.rect((staff.unit(-0.5), staff.unit(-1)), c1, staff.unit(2.75), staff.unit(6), brush=Brush.no_brush())
    dur = random.randint(2, 9)
    arrow1 = Path.arrow((staff.unit(2.5), staff.unit(2)), c1,
                        (staff.unit(dur), staff.unit(0)), brush="#10ada080", pen=Pen("#10ada080", Mm(1)))
    arrow2 = Path.arrow((staff.unit(-0.75), staff.unit(2)), c1,
                        (staff.unit(-dur), staff.unit(0)), brush="#10ada080", pen=Pen("#10ada080", Mm(1)))
    length = Unit(staff.unit(3+2*dur))
    return length


def triad_rank_3(staff, x):
    c1 = Chordrest(staff.unit(x), staff, ["d", "f", "a"], (1, 1))
    for n in c1.noteheads:
        n.brush = "#10ada0"
    box = Path.rect((staff.unit(-0.5), staff.unit(-1)), c1, staff.unit(2.75), staff.unit(7), brush=Brush.no_brush())
    dur = random.randint(2, 9)
    arrow1 = Path.arrow((staff.unit(2.5), staff.unit(2)), c1,
                        (staff.unit(dur), staff.unit(0)), brush="#10ada080", pen=Pen("#10ada080", Mm(1)))
    arrow2 = Path.arrow((staff.unit(-0.75), staff.unit(2)), c1,
                        (staff.unit(-dur), staff.unit(0)), brush="#10ada080", pen=Pen("#10ada080", Mm(1)))
    length = Unit(staff.unit(3+2*dur))
    return length


def triad_rank_4(staff, x):
    c1 = Chordrest(staff.unit(x), staff, ["f", "a", "c'", "e'"], (1, 1))
    for n in c1.noteheads:
        n.brush = "#10ada0"
    box = Path.rect((staff.unit(-0.5), staff.unit(-1)), c1, staff.unit(2.75), staff.unit(6), brush=Brush.no_brush())
    dur = random.randint(2, 9)
    arrow1 = Path.arrow((staff.unit(2.5), staff.unit(2)), c1,
                        (staff.unit(dur), staff.unit(0)), brush="#10ada080", pen=Pen("#10ada080", Mm(1)))
    arrow2 = Path.arrow((staff.unit(-0.75), staff.unit(2)), c1,
                        (staff.unit(-dur), staff.unit(0)), brush="#10ada080", pen=Pen("#10ada080", Mm(1)))
    length = Unit(staff.unit(3+2*dur))
    return length


def melody_rank_1(staff, x):
    n1 = Notehead(staff.unit(x), staff, "f'", Duration(1, 4))
    n1.brush = "#b221de"
    a1 = Accidental((staff.unit(-1.25), staff.unit(0)), n1, "accidentalSharp")
    a1.brush = "#b221de"
    n2 = Notehead(staff.unit(3), n1, "e'", Duration(1, 4))
    n2.brush = "#b221de"
    n3 = Notehead(staff.unit(3), n2, "d'", Duration(1, 4))
    n3.brush = "#b221de"
    n4 = Notehead(staff.unit(3), n3, "f'", Duration(1, 4))
    n4.brush = "#b221de"
    a4 = Accidental((staff.unit(-1.25), staff.unit(0)), n4, "accidentalSharp")
    a4.brush = "#b221de"
    n5 = Notehead(staff.unit(3), n4, "g'", Duration(1, 4))
    n5.brush = "#b221de"
    n6 = Notehead(staff.unit(3), n5, "f'", Duration(1, 4))
    n6.brush = "#b221de"
    a6 = Accidental((staff.unit(-1.25), staff.unit(0)), n6, "accidentalSharp")
    a6.brush = "#b221de"
    length = Unit(staff.unit(18))
    return length


def melody_rank_2(staff, x):
    n1 = Notehead(staff.unit(x), staff, "f'", Duration(1, 4))
    n1.brush = "#b221de"
    a1 = Accidental((staff.unit(-1.25), staff.unit(0)), n1, "accidentalSharp")
    a1.brush = "#b221de"
    n2 = Notehead(staff.unit(3), n1, "e'", Duration(1, 4))
    n2.brush = "#b221de"
    n3 = Notehead(staff.unit(3), n2, "d'", Duration(1, 4))
    n3.brush = "#b221de"
    n4 = Notehead(staff.unit(3), n3, "c'", Duration(1, 4))
    n4.brush = "#b221de"
    a4 = Accidental((staff.unit(-1.25), staff.unit(0)), n4, "accidentalSharp")
    a4.brush = "#b221de"
    n5 = Notehead(staff.unit(3), n4, "b", Duration(1, 4))
    n5.brush = "#b221de"
    n6 = Notehead(staff.unit(3), n5, "a", Duration(1, 4))
    n6.brush = "#b221de"
    n7 = Notehead(staff.unit(3), n6, "b", Duration(1, 4))
    n7.brush = "#b221de"
    length = Unit(staff.unit(21))
    return length


def melody_rank_3(staff, x):
    n1 = Notehead(staff.unit(x), staff, "b", Duration(1, 4))
    n1.brush = "#b221de"
    n2 = Notehead(staff.unit(3), n1, "d'", Duration(1, 4))
    n2.brush = "#b221de"
    n3 = Notehead(staff.unit(3), n2, "f'", Duration(1, 4))
    n3.brush = "#b221de"
    a3 = Accidental((staff.unit(-1.25), staff.unit(0)), n3, "accidentalSharp")
    a3.brush = "#b221de"
    n4 = Notehead(staff.unit(3), n3, "e'", Duration(1, 4))
    n4.brush = "#b221de"
    n5 = Notehead(staff.unit(3), n4, "d'", Duration(1, 4))
    n5.brush = "#b221de"
    n6 = Notehead(staff.unit(3), n5, "c'", Duration(1, 4))
    n6.brush = "#b221de"
    a6 = Accidental((staff.unit(-1.25), staff.unit(0)), n6, "accidentalSharp")
    a6.brush = "#b221de"
    length = Unit(staff.unit(18))
    return length


def melody_rank_4(staff, x):
    n1 = Notehead(staff.unit(x), staff, "b", Duration(1, 4))
    n1.brush = "#b221de"
    n2 = Notehead(staff.unit(3), n1, "d'", Duration(1, 4))
    n2.brush = "#b221de"
    n3 = Notehead(staff.unit(3), n2, "c'", Duration(1, 4))
    n3.brush = "#b221de"
    a3 = Accidental((staff.unit(-1.25), staff.unit(0)), n3, "accidentalSharp")
    a3.brush = "#b221de"
    n4 = Notehead(staff.unit(3), n3, "a", Duration(1, 4))
    n4.brush = "#b221de"
    n5 = Notehead(staff.unit(3), n4, "b", Duration(1, 4))
    n5.brush = "#b221de"
    length = Unit(staff.unit(15))
    return length


def harmonic_rank_1(staff, x):
    guitar_string = random.choice(["guitarString1", "guitarString2", "guitarString3",
                                   "guitarString4", "guitarString5", "guitarString6"])
    diamond = Path((staff.unit(x)+staff.unit(1), staff.unit(0)), staff, "#ff00ff55")
    diamond.line_to(staff.unit(1), staff.unit(2))
    diamond.line_to(staff.unit(0), staff.unit(4))
    diamond.line_to(staff.unit(-1), staff.unit(2))
    diamond.line_to(staff.unit(0), staff.unit(0))
    c1 = Text((staff.unit(-1.5), staff.unit(-2.75)), diamond, "XII", neoscore.default_font.modified(weight=80),
              "#ff00ff")
    m1 = MusicText(
        (staff.unit(-1), staff.unit(-0.25)),
        diamond,
        guitar_string, None, "#ff00ff"
    )
    c2 = Text((staff.unit(1.5), staff.unit(6.5)), diamond, "XII", neoscore.default_font.modified(weight=80), "#ff00ff")
    m2 = MusicText(
        (staff.unit(1), staff.unit(4.25)),
        diamond,
        guitar_string, None, "#ff00ff"
    )
    c2.rotation = 180
    m2.rotation = 180
    length = Unit(staff.unit(3))
    return length


def harmonic_rank_2(staff, x):
    guitar_string = random.choice(["guitarString1", "guitarString2", "guitarString3",
                                   "guitarString4", "guitarString5", "guitarString6"])
    diamond = Path((staff.unit(x)+staff.unit(1), staff.unit(0)), staff, "#ff00ff55")
    diamond.line_to(staff.unit(1), staff.unit(2))
    diamond.line_to(staff.unit(0), staff.unit(4))
    diamond.line_to(staff.unit(-1), staff.unit(2))
    diamond.line_to(staff.unit(0), staff.unit(0))
    c1 = Text((staff.unit(-1.5), staff.unit(-2.75)), diamond, "VII", neoscore.default_font.modified(weight=80),
              "#ff00ff")
    m1 = MusicText(
        (staff.unit(-1), staff.unit(-0.25)),
        diamond,
        guitar_string, None, "#ff00ff"
    )
    c2 = Text((staff.unit(1.5), staff.unit(6.5)), diamond, "VII", neoscore.default_font.modified(weight=80), "#ff00ff")
    m2 = MusicText(
        (staff.unit(1), staff.unit(4.25)),
        diamond,
        guitar_string, None, "#ff00ff"
    )
    c2.rotation = 180
    m2.rotation = 180
    length = Unit(staff.unit(3))
    return length


def harmonic_rank_3(staff, x):
    guitar_string = random.choice(["guitarString1", "guitarString2", "guitarString3",
                                   "guitarString4", "guitarString5", "guitarString6"])
    diamond = Path((staff.unit(x)+staff.unit(1), staff.unit(0)), staff, "#ff00ff55")
    diamond.line_to(staff.unit(1), staff.unit(2))
    diamond.line_to(staff.unit(0), staff.unit(4))
    diamond.line_to(staff.unit(-1), staff.unit(2))
    diamond.line_to(staff.unit(0), staff.unit(0))
    c1 = Text((staff.unit(-0.75), staff.unit(-2.75)), diamond, "V", neoscore.default_font.modified(weight=80),
              "#ff00ff")
    m1 = MusicText(
        (staff.unit(-1), staff.unit(-0.25)),
        diamond,
        guitar_string, None, "#ff00ff"
    )
    c2 = Text((staff.unit(0.75), staff.unit(6.5)), diamond, "V", neoscore.default_font.modified(weight=80), "#ff00ff")
    m2 = MusicText(
        (staff.unit(1), staff.unit(4.25)),
        diamond,
        guitar_string, None, "#ff00ff"
    )
    c2.rotation = 180
    m2.rotation = 180
    length = Unit(staff.unit(3))
    return length


def harmonic_rank_4(staff, x):
    guitar_string = random.choice(["guitarString1", "guitarString2", "guitarString3",
                                   "guitarString4", "guitarString5", "guitarString6"])
    diamond = Path((staff.unit(x)+staff.unit(8), staff.unit(0)), staff, "#ff00ff55")
    diamond.line_to(staff.unit(1), staff.unit(2))
    diamond.line_to(staff.unit(0), staff.unit(4))
    diamond.line_to(staff.unit(-1), staff.unit(2))
    diamond.line_to(staff.unit(0), staff.unit(0))
    c1 = Text((staff.unit(-1.25), staff.unit(-2.75)), diamond, "IX", neoscore.default_font.modified(weight=80),
              "#ff00ff")
    m1 = MusicText(
        (staff.unit(-1), staff.unit(-0.25)),
        diamond,
        guitar_string, None, "#ff00ff"
    )
    c2 = Text((staff.unit(1.75), staff.unit(6.5)), diamond, "IX", neoscore.default_font.modified(weight=80), "#ff00ff")
    m2 = MusicText(
        (staff.unit(1), staff.unit(4.25)),
        diamond,
        guitar_string, None, "#ff00ff"
    )
    c2.rotation = 180
    m2.rotation = 180
    length = Unit(staff.unit(3))
    return length


def rake_rank_1(staff, x):
    c1 = Text((staff.unit(x), staff.unit(-2)), staff, "CVI (RH~19)", None, "#c391c4")
    RepeatingMusicTextLine((staff.unit(0), staff.unit(1)), c1,
                           (staff.unit(0), staff.unit(8)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    RepeatingMusicTextLine((staff.unit(12), staff.unit(1)), c1,
                           (staff.unit(12), staff.unit(8)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    c2 = Text((staff.unit(13), staff.unit(8)), c1, "CVI (RH~19)", None, "#c391c4")
    c2.rotation = 180
    length = Unit(staff.unit(14))
    return length


def rake_rank_2(staff, x):
    c1 = Text((staff.unit(x), staff.unit(-2)), staff, "CIV (RH~24)", None, "#c391c4")
    RepeatingMusicTextLine((staff.unit(0), staff.unit(1)), c1,
                           (staff.unit(0), staff.unit(8)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    RepeatingMusicTextLine((staff.unit(12), staff.unit(1)), c1,
                           (staff.unit(12), staff.unit(8)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    c2 = Text((staff.unit(13), staff.unit(8)), c1, "CIV (RH~24)", None, "#c391c4")
    c2.rotation = 180
    length = Unit(staff.unit(14))
    return length


def rake_rank_3(staff, x):
    c1 = Text((staff.unit(x), staff.unit(-2)), staff, "CVII (RH~19)", None, "#c391c4")
    RepeatingMusicTextLine((staff.unit(0), staff.unit(1)), c1,
                           (staff.unit(0), staff.unit(8)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    RepeatingMusicTextLine((staff.unit(12), staff.unit(1)), c1,
                           (staff.unit(12), staff.unit(8)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    c2 = Text((staff.unit(13), staff.unit(8)), c1, "CVII (RH~19", None, "#c391c4")
    c2.rotation = 180
    length = Unit(staff.unit(14))
    return length


def rake_rank_4(staff, x):
    c1 = Text((staff.unit(x), staff.unit(-2)), staff, "G5", None, "#c391c4")
    RepeatingMusicTextLine((staff.unit(0), staff.unit(1)), c1,
                           (staff.unit(0), staff.unit(3)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    RepeatingMusicTextLine((staff.unit(2), staff.unit(2)), c1,
                           (staff.unit(2), staff.unit(4)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    RepeatingMusicTextLine((staff.unit(4), staff.unit(3)), c1,
                           (staff.unit(4), staff.unit(5)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    RepeatingMusicTextLine((staff.unit(6), staff.unit(4)), c1,
                           (staff.unit(6), staff.unit(6)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    RepeatingMusicTextLine((staff.unit(8), staff.unit(5)), c1,
                           (staff.unit(8), staff.unit(7)), c1,
                           "wiggleTrillFastest", brush="#c391c4")
    c2 = Text((staff.unit(9), staff.unit(8)), c1, "G5", None, "#c391c4")
    c2.rotation = 180
    length = Unit(staff.unit(10))
    return length


def rasg_rank_1(staff, x):
    def chord_diagram(parent):
        MusicText(
            (staff.unit(0.05), staff.unit(-4.5)),
            parent,
            "fretboardO", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(0.725), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(1.4), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(2.075), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(2.75), staff.unit(-4.5)),
            parent,
            "fretboardO", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(3.425), staff.unit(-4.5)),
            parent,
            "fretboardO", None, "#f51d1d"
        )
        i = random.randint(0, 3)
    t1 = Text((staff.unit(x), staff.unit(2)), staff, "R", neoscore.default_font.modified(size=Unit(20), weight=80,
                                                                                         italic=True), "#f51d1d")
    t2 = Text((staff.unit(x)+staff.unit(3), staff.unit(2)), staff, "R",
              neoscore.default_font.modified(size=Unit(20), weight=80, italic=True), "#f51d1d")
    t2.rotation = 180
    diagram_1 = MusicText(
        (staff.unit(-0.5), staff.unit(-4)),
        t1,
        "fretboard6String", None, "#f51d1d"
    )
    chord_diagram(diagram_1)
    diagram_2 = MusicText(
        (staff.unit(3.5), staff.unit(4)),
        t1,
        "fretboard6String", None, "#f51d1d"
    )
    chord_diagram(diagram_2)
    diagram_2.rotation = 180
    length = Unit(staff.unit(6))
    return length


def rasg_rank_2(staff, x):
    def chord_diagram(parent):
        MusicText(
            (staff.unit(0.05), staff.unit(-4.5)),
            parent,
            "fretboardX", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(0.725), staff.unit(-4.5)),
            parent,
            "fretboardO", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(1.4), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(2.075), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(2.75), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(3.425), staff.unit(-4.5)),
            parent,
            "fretboardO", None, "#f51d1d"
        )
        i = random.randint(0, 3)

    t1 = Text((staff.unit(x), staff.unit(2)), staff, "R", neoscore.default_font.modified(size=Unit(20), weight=80,
                                                                                         italic=True), "#f51d1d")
    t2 = Text((staff.unit(x) + staff.unit(3), staff.unit(2)), staff, "R",
              neoscore.default_font.modified(size=Unit(20), weight=80, italic=True), "#f51d1d")
    t2.rotation = 180
    diagram_1 = MusicText(
        (staff.unit(-0.5), staff.unit(-4)),
        t1,
        "fretboard6String", None, "#f51d1d"
    )
    chord_diagram(diagram_1)
    diagram_2 = MusicText(
        (staff.unit(3.5), staff.unit(4)),
        t1,
        "fretboard6String", None, "#f51d1d"
    )
    chord_diagram(diagram_2)
    diagram_2.rotation = 180
    length = Unit(staff.unit(6))
    return length


def rasg_rank_3(staff, x):
    def chord_diagram(parent):
        MusicText(
            (staff.unit(0.05), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(0.725), staff.unit(-1.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(1.4), staff.unit(-1.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(2.075), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(2.75), staff.unit(-4.5)),
            parent,
            "fretboardO", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(3.425), staff.unit(-4.5)),
            parent,
            "fretboardO", None, "#f51d1d"
        )
        i = random.randint(0, 3)

    t1 = Text((staff.unit(x), staff.unit(2)), staff, "R", neoscore.default_font.modified(size=Unit(20), weight=80,
                                                                                         italic=True), "#f51d1d")
    t2 = Text((staff.unit(x) + staff.unit(3), staff.unit(2)), staff, "R",
              neoscore.default_font.modified(size=Unit(20), weight=80, italic=True), "#f51d1d")
    t2.rotation = 180
    diagram_1 = MusicText(
        (staff.unit(-0.5), staff.unit(-4)),
        t1,
        "fretboard6String", None, "#f51d1d"
    )
    chord_diagram(diagram_1)
    diagram_2 = MusicText(
        (staff.unit(3.5), staff.unit(4)),
        t1,
        "fretboard6String", None, "#f51d1d"
    )
    chord_diagram(diagram_2)
    diagram_2.rotation = 180
    length = Unit(staff.unit(6))
    return length


def rasg_rank_4(staff, x):
    def chord_diagram(parent):
        MusicText(
            (staff.unit(0.05), staff.unit(-4.5)),
            parent,
            "fretboardX", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(0.725), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(1.4), staff.unit(-1.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(2.075), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(2.75), staff.unit(-1.5)),
            parent,
            "fretboardFilledCircle", None, "#f51d1d"
        )
        MusicText(
            (staff.unit(3.425), staff.unit(-4.5)),
            parent,
            "fretboardO", None, "#f51d1d"
        )
        i = random.randint(0, 3)

    t1 = Text((staff.unit(x), staff.unit(2)), staff, "R", neoscore.default_font.modified(size=Unit(20), weight=80,
                                                                                         italic=True), "#f51d1d")
    t2 = Text((staff.unit(x) + staff.unit(3), staff.unit(2)), staff, "R",
              neoscore.default_font.modified(size=Unit(20), weight=80, italic=True), "#f51d1d")
    t2.rotation = 180
    diagram_1 = MusicText(
        (staff.unit(-0.5), staff.unit(-4)),
        t1,
        "fretboard6String", None, "#f51d1d"
    )
    chord_diagram(diagram_1)
    diagram_2 = MusicText(
        (staff.unit(3.5), staff.unit(4)),
        t1,
        "fretboard6String", None, "#f51d1d"
    )
    chord_diagram(diagram_2)
    diagram_2.rotation = 180
    length = Unit(staff.unit(6))
    return length


def tremolo_rank_1(staff, x):
    n1 = Chordrest(staff.unit(x), staff, ["e'"], (1, 16))
    n2 = Chordrest(staff.unit(x)+staff.unit(2), staff, ["a'"], (1, 16))
    n3 = Chordrest(staff.unit(x)+staff.unit(4), staff, ["a'"], (1, 16))
    n4 = Chordrest(staff.unit(x)+staff.unit(6), staff, ["a'"], (1, 16))
    n = [n1, n2, n3, n4]
    for i in n1.noteheads:
        i.brush = "#0073c4"
    for i in n2.noteheads:
        i.brush = "#0073c4"
    for i in n3.noteheads:
        i.brush = "#0073c4"
    for i in n4.noteheads:
        i.brush = "#0073c4"
    BeamGroup(n, brush="#0073c499", pen="#0073c499")
    box = Path.rect((staff.unit(-1), staff.unit(-3)), n1, staff.unit(9), staff.unit(8), brush=Brush.no_brush(),
                    pen="#0073c4")
    dur = random.randint(2, 9)
    arrow1 = Path.arrow((staff.unit(9.25), staff.unit(4)), box,
                        (staff.unit(dur), staff.unit(0)), pen=Pen("#0073c455", Mm(1)), brush="#0073c455")
    arrow2 = Path.arrow((staff.unit(-0.25), staff.unit(4)), box,
                        (staff.unit(-dur), staff.unit(0)), pen=Pen("#0073c455", Mm(1)), brush="#0073c455")
    length = Unit(staff.unit(2*dur + 9))
    return length


def tremolo_rank_2(staff, x):
    n1 = Chordrest(staff.unit(x), staff, ["d'"], (1, 16))
    n2 = Chordrest(staff.unit(x)+staff.unit(2), staff, ["a'"], (1, 16))
    n3 = Chordrest(staff.unit(x)+staff.unit(4), staff, ["a'"], (1, 16))
    n4 = Chordrest(staff.unit(x)+staff.unit(6), staff, ["a'"], (1, 16))
    n = [n1, n2, n3, n4]
    for i in n1.noteheads:
        i.brush = "#0073c4"
    for i in n2.noteheads:
        i.brush = "#0073c4"
    for i in n3.noteheads:
        i.brush = "#0073c4"
    for i in n4.noteheads:
        i.brush = "#0073c4"
    BeamGroup(n, brush="#0073c499", pen="#0073c499")
    box = Path.rect((staff.unit(-1), staff.unit(-2.5)), n1, staff.unit(9), staff.unit(8),
                    brush=Brush.no_brush(), pen="#0073c4")
    dur = random.randint(2, 9)
    arrow1 = Path.arrow((staff.unit(9.25), staff.unit(4)), box,
                        (staff.unit(dur), staff.unit(0)), pen=Pen("#0073c455", Mm(1)), brush="#0073c455")
    arrow2 = Path.arrow((staff.unit(-0.25), staff.unit(4)), box,
                        (staff.unit(-dur), staff.unit(0)), pen=Pen("#0073c455", Mm(1)), brush="#0073c455")
    length = Unit(staff.unit(2*dur + 9))
    return length


def tremolo_rank_3(staff, x):
    n1 = Chordrest(staff.unit(x), staff, ["b"], (1, 16))
    n2 = Chordrest(staff.unit(x)+staff.unit(2), staff, ["b"], (1, 16))
    n3 = Chordrest(staff.unit(x)+staff.unit(4), staff, ["b"], (1, 16))
    n4 = Chordrest(staff.unit(x)+staff.unit(6), staff, ["b"], (1, 16))
    n = [n1, n2, n3, n4]
    for i in n1.noteheads:
        i.brush = "#0073c4"
    for i in n2.noteheads:
        i.brush = "#0073c4"
    for i in n3.noteheads:
        i.brush = "#0073c4"
    for i in n4.noteheads:
        i.brush = "#0073c4"
    BeamGroup(n, brush="#0073c499", pen="#0073c499")
    box = Path.rect((staff.unit(-1), staff.unit(-0.5)), n1, staff.unit(9), staff.unit(8),
                    brush=Brush.no_brush(), pen="#0073c4")
    dur = random.randint(2, 9)
    arrow1 = Path.arrow((staff.unit(9.25), staff.unit(4)), box,
                        (staff.unit(dur), staff.unit(0)), pen=Pen("#0073c455", Mm(1)), brush="#0073c455")
    arrow2 = Path.arrow((staff.unit(-0.25), staff.unit(4)), box,
                        (staff.unit(-dur), staff.unit(0)), pen=Pen("#0073c455", Mm(1)), brush="#0073c455")
    length = Unit(staff.unit(2*dur + 9))
    return length


def tremolo_rank_4(staff, x):
    n1 = Chordrest(staff.unit(x), staff, ["b"], (1, 16))
    n2 = Chordrest(staff.unit(x)+staff.unit(2), staff, ["e'"], (1, 16))
    n3 = Chordrest(staff.unit(x)+staff.unit(4), staff, ["d'"], (1, 16))
    n4 = Chordrest(staff.unit(x)+staff.unit(6), staff, ["d'"], (1, 16))
    n = [n1, n2, n3, n4]
    for i in n1.noteheads:
        i.brush = "#0073c4"
    for i in n2.noteheads:
        i.brush = "#0073c4"
    for i in n3.noteheads:
        i.brush = "#0073c4"
    for i in n4.noteheads:
        i.brush = "#0073c4"
    BeamGroup(n, brush="#0073c499", pen="#0073c499")
    box = Path.rect((staff.unit(-1), staff.unit(-1.5)), n1, staff.unit(9), staff.unit(8),
                    brush=Brush.no_brush(), pen="#0073c4")
    dur = random.randint(2, 9)
    arrow1 = Path.arrow((staff.unit(9.25), staff.unit(4)), box,
                        (staff.unit(dur), staff.unit(0)), pen=Pen("#0073c455", Mm(1)), brush="#0073c455")
    arrow2 = Path.arrow((staff.unit(-0.25), staff.unit(4)), box,
                        (staff.unit(-dur), staff.unit(0)), pen=Pen("#0073c455", Mm(1)), brush="#0073c455")
    length = Unit(staff.unit(2*dur + 9))
    return length


def adv_harm_rank_1(staff, x):
    def chord_diagram(parent):
        MusicText(
            (staff.unit(0.05), staff.unit(-4.5)),
            parent,
            "fretboardX", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(0.725), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(1.4), staff.unit(-1.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(2.075), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(2.75), staff.unit(-1.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(3.425), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        i = random.randint(0, 3)
        Text((staff.unit(-1), staff.unit(-6)), parent, ["BMaj7", "CMaj7", "DMaj7", "EMaj7"][i], None, "#4b8c27")
        Text((staff.unit(4), staff.unit(-2.5)), parent, ["II", "III", "V", "VII"][i], None, "#4b8c27")

    path = Path((staff.unit(x), staff.unit(0)), staff, "#4b8c2755")
    path.line_to(staff.unit(2), staff.unit(4))
    path.line_to(staff.unit(0), staff.unit(4))
    path.line_to(staff.unit(2), staff.unit(0))
    path.line_to(staff.unit(0), staff.unit(0))
    diagram_1 = MusicText(
        (staff.unit(-1), staff.unit(-1)),
        path,
        "fretboard6String", None, "#4b8c27"
    )
    chord_diagram(diagram_1)
    diagram_2 = MusicText(
        (staff.unit(3), staff.unit(5)),
        path,
        "fretboard6String", None, "#4b8c27"
    )
    chord_diagram(diagram_2)
    diagram_2.rotation = 180
    length = Unit(staff.unit(5))
    return length


def adv_harm_rank_2(staff, x):
    def chord_diagram(parent):
        MusicText(
            (staff.unit(0.05), staff.unit(-4.5)),
            parent,
            "fretboardX", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(0.725), staff.unit(-4.5)),
            parent,
            "fretboardX", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(1.4), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(2.075), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(2.75), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(3.425), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        i = random.randint(0, 3)
        Text((staff.unit(-1), staff.unit(-6)), parent, ["Fo7", "F#o7", "Go7", "G#o7", "Ao7", "Bbo7", "Co7"][i],
             None, "#4b8c27")
        Text((staff.unit(4), staff.unit(-2.5)), parent, ["III", "IV", "V", "VI", "VII", "IX"][i], None, "#4b8c27")

    path = Path((staff.unit(x), staff.unit(0)), staff, "#4b8c2755")
    path.line_to(staff.unit(2), staff.unit(4))
    path.line_to(staff.unit(0), staff.unit(4))
    path.line_to(staff.unit(2), staff.unit(0))
    path.line_to(staff.unit(0), staff.unit(0))
    diagram_1 = MusicText(
        (staff.unit(-1), staff.unit(-1)),
        path,
        "fretboard6String", None, "#4b8c27"
    )
    chord_diagram(diagram_1)
    diagram_2 = MusicText(
        (staff.unit(3), staff.unit(5)),
        path,
        "fretboard6String", None, "#4b8c27"
    )
    chord_diagram(diagram_2)
    diagram_2.rotation = 180
    length = Unit(staff.unit(5))
    return length


def adv_harm_rank_3(staff, x):
    def chord_diagram(parent):
        MusicText(
            (staff.unit(0.05), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(0.725), staff.unit(-1.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(1.4), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(2.075), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(2.75), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(3.425), staff.unit(-1.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        i = random.randint(0, 3)
        Text((staff.unit(0), staff.unit(-6)), parent, ["F#9", "G9", "Ab9", "A9", "Bb9", "C9"][i], None, "#4b8c27")
        Text((staff.unit(4), staff.unit(-2.5)), parent, ["II", "III", "IV", "V", "VI", "VII"][i], None, "#4b8c27")

    path = Path((staff.unit(x), staff.unit(0)), staff, "#4b8c2755")
    path.line_to(staff.unit(2), staff.unit(4))
    path.line_to(staff.unit(0), staff.unit(4))
    path.line_to(staff.unit(2), staff.unit(0))
    path.line_to(staff.unit(0), staff.unit(0))
    diagram_1 = MusicText(
        (staff.unit(-1), staff.unit(-1)),
        path,
        "fretboard6String", None, "#4b8c27"
    )
    chord_diagram(diagram_1)
    diagram_2 = MusicText(
        (staff.unit(3), staff.unit(5)),
        path,
        "fretboard6String", None, "#4b8c27"
    )
    chord_diagram(diagram_2)
    diagram_2.rotation = 180
    length = Unit(staff.unit(5))
    return length


def adv_harm_rank_4(staff, x):
    def chord_diagram(parent):
        MusicText(
            (staff.unit(0.05), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(0.725), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(1.4), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(2.075), staff.unit(-3.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(2.75), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        MusicText(
            (staff.unit(3.425), staff.unit(-2.5)),
            parent,
            "fretboardFilledCircle", None, "#4b8c27"
        )
        i = random.randint(0, 3)
        Text((staff.unit(0), staff.unit(-6)), parent,
             ["F#Q", "GQ", "AbQ", "AQ", "BbQ", "CQ", "C#Q", "DQ", "EbQ"][i], None, "#4b8c27")
        Text((staff.unit(4), staff.unit(-2.5)), parent,
             ["II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"][i], None, "#4b8c27")

    path = Path((staff.unit(x), staff.unit(0)), staff, "#4b8c2755")
    path.line_to(staff.unit(2), staff.unit(4))
    path.line_to(staff.unit(0), staff.unit(4))
    path.line_to(staff.unit(2), staff.unit(0))
    path.line_to(staff.unit(0), staff.unit(0))
    diagram_1 = MusicText(
        (staff.unit(-1), staff.unit(-1)),
        path,
        "fretboard6String", None, "#4b8c27"
    )
    chord_diagram(diagram_1)
    diagram_2 = MusicText(
        (staff.unit(3), staff.unit(5)),
        path,
        "fretboard6String", None, "#4b8c27"
    )
    chord_diagram(diagram_2)
    diagram_2.rotation = 180
    length = Unit(staff.unit(5))
    return length


if __name__ == '__main__':
    neoscore.setup()

    neoscore.document.pages[1]

    y = Unit(0)

    staff_1 = Staff((Inch(0.5), Inch(1)), parent=None, length=Inch(1))
    clef_1 = InvisibleClef(Unit(0), staff_1, 'treble')
    scrape_rank_1(staff_1, y)

    staff_2 = Staff((Inch(2), Inch(1)), parent=None, length=Inch(1))
    clef_2 = InvisibleClef(Unit(0), staff_2, 'treble')
    scrape_rank_2(staff_2, y)

    staff_3 = Staff((Inch(3.5), Inch(1)), parent=None, length=Inch(1))
    clef_3 = InvisibleClef(Unit(0), staff_3, 'treble')
    scrape_rank_3(staff_3, y)

    staff_4 = Staff((Inch(5), Inch(1)), parent=None, length=Inch(1))
    clef_4 = InvisibleClef(Unit(0), staff_4, 'treble')
    scrape_rank_4(staff_4, y)

    staff_5 = Staff((Inch(0.5), Inch(2.5)), parent=None, length=Inch(1))
    clef_5 = InvisibleClef(Unit(0), staff_5, 'treble')
    bartok_rank_1(staff_5, y)

    staff_6 = Staff((Inch(2), Inch(2.5)), parent=None, length=Inch(1))
    clef_6 = InvisibleClef(Unit(0), staff_6, 'treble')
    bartok_rank_2(staff_6, y)

    staff_7 = Staff((Inch(3.5), Inch(2.5)), parent=None, length=Inch(1))
    clef_7 = InvisibleClef(Unit(0), staff_7, 'treble')
    bartok_rank_3(staff_7, y)

    staff_8 = Staff((Inch(5), Inch(2.5)), parent=None, length=Inch(1))
    clef_8 = InvisibleClef(Unit(0), staff_8, 'treble')
    bartok_rank_4(staff_8, y)

    staff_9 = Staff((Inch(0.5), Inch(4)), parent=None, length=Inch(1))
    clef_9 = InvisibleClef(Unit(0), staff_9, 'treble')
    tambura_rank_1(staff_9, y)

    staff_10 = Staff((Inch(2), Inch(4)), parent=None, length=Inch(1))
    clef_10 = InvisibleClef(Unit(0), staff_10, 'treble')
    tambura_rank_2(staff_10, y)

    staff_11 = Staff((Inch(3.5), Inch(4)), parent=None, length=Inch(1))
    clef_11 = InvisibleClef(Unit(0), staff_11, 'treble')
    tambura_rank_3(staff_11, y)

    staff_12 = Staff((Inch(5), Inch(4)), parent=None, length=Inch(1))
    clef_12 = InvisibleClef(Unit(0), staff_12, 'treble')
    tambura_rank_4(staff_12, y)

    staff_13 = Staff((Inch(0.5), Inch(5.5)), parent=None, length=Inch(1))
    clef_13 = InvisibleClef(Unit(0), staff_13, 'treble')
    perc_rank_1(staff_13, y)

    staff_14 = Staff((Inch(2), Inch(5.5)), parent=None, length=Inch(1))
    clef_14 = InvisibleClef(Unit(0), staff_14, 'treble')
    perc_rank_2(staff_14, y)

    staff_15 = Staff((Inch(3.5), Inch(5.5)), parent=None, length=Inch(1))
    clef_15 = InvisibleClef(Unit(0), staff_15, 'treble')
    perc_rank_3(staff_15, y)

    staff_16 = Staff((Inch(5), Inch(5.5)), parent=None, length=Inch(1))
    clef_16 = InvisibleClef(Unit(0), staff_16, 'treble')
    perc_rank_4(staff_16, y)

    staff_17 = Staff((Inch(0.5), Inch(6.5)), parent=None, length=Inch(1))
    clef_17 = InvisibleClef(Unit(0), staff_17, 'treble')
    triad_rank_1(staff_17, y)

    staff_18 = Staff((Inch(2), Inch(6.5)), parent=None, length=Inch(1))
    clef_18 = InvisibleClef(Unit(0), staff_18, 'treble')
    triad_rank_2(staff_18, y)

    staff_19 = Staff((Inch(3.5), Inch(6.5)), parent=None, length=Inch(1))
    clef_19 = InvisibleClef(Unit(0), staff_19, 'treble')
    triad_rank_3(staff_19, y)

    staff_20 = Staff((Inch(5), Inch(6.5)), parent=None, length=Inch(1))
    clef_20 = InvisibleClef(Unit(0), staff_20, 'treble')
    triad_rank_4(staff_20, y)

    staff_21 = Staff((Inch(0.5), Inch(7.5)), parent=None, length=Inch(1))
    clef_21 = InvisibleClef(Unit(0), staff_21, 'treble')
    melody_rank_1(staff_21, y)

    staff_22 = Staff((Inch(2), Inch(7.5)), parent=None, length=Inch(1))
    clef_22 = InvisibleClef(Unit(0), staff_22, 'treble')
    melody_rank_2(staff_22, y)

    staff_23 = Staff((Inch(3.5), Inch(7.5)), parent=None, length=Inch(1))
    clef_23 = InvisibleClef(Unit(0), staff_23, 'treble')
    melody_rank_3(staff_23, y)

    staff_24 = Staff((Inch(5), Inch(7.5)), parent=None, length=Inch(1))
    clef_24 = InvisibleClef(Unit(0), staff_24, 'treble')
    melody_rank_4(staff_24, y)

    staff_25 = Staff((Inch(0.5), Inch(8.5)), parent=None, length=Inch(1))
    clef_25 = InvisibleClef(Unit(0), staff_25, 'treble')
    harmonic_rank_1(staff_25, y)

    staff_26 = Staff((Inch(2), Inch(8.5)), parent=None, length=Inch(1))
    clef_26 = InvisibleClef(Unit(0), staff_26, 'treble')
    harmonic_rank_2(staff_26, y)

    staff_27 = Staff((Inch(3.5), Inch(8.5)), parent=None, length=Inch(1))
    clef_27 = InvisibleClef(Unit(0), staff_27, 'treble')
    harmonic_rank_3(staff_27, y)

    staff_28 = Staff((Inch(5), Inch(8.5)), parent=None, length=Inch(1))
    clef_28 = InvisibleClef(Unit(0), staff_28, 'treble')
    harmonic_rank_4(staff_28, y)

    staff_29 = Staff((Inch(0.5), Inch(9.5)), parent=None, length=Inch(1))
    clef_29 = InvisibleClef(Unit(0), staff_29, 'treble')
    rake_rank_1(staff_29, y)

    staff_30 = Staff((Inch(2), Inch(9.5)), parent=None, length=Inch(1))
    clef_30 = InvisibleClef(Unit(0), staff_30, 'treble')
    rake_rank_2(staff_30, y)

    staff_31 = Staff((Inch(3.5), Inch(9.5)), parent=None, length=Inch(1))
    clef_31 = InvisibleClef(Unit(0), staff_31, 'treble')
    rake_rank_3(staff_31, y)

    staff_32 = Staff((Inch(5), Inch(9.5)), parent=None, length=Inch(1))
    clef_32 = InvisibleClef(Unit(0), staff_32, 'treble')
    rake_rank_4(staff_32, y)

    staff_33 = Staff((Inch(0.5), Inch(0.5)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_33 = InvisibleClef(Unit(0), staff_33, 'treble')
    rasg_rank_1(staff_33, y)

    staff_34 = Staff((Inch(2), Inch(0.5)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_34 = InvisibleClef(Unit(0), staff_34, 'treble')
    rasg_rank_2(staff_34, y)

    staff_35 = Staff((Inch(3.5), Inch(0.5)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_35 = InvisibleClef(Unit(0), staff_35, 'treble')
    rasg_rank_3(staff_35, y)

    staff_36 = Staff((Inch(5), Inch(0.5)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_36 = InvisibleClef(Unit(0), staff_36, 'treble')
    rasg_rank_4(staff_36, y)

    staff_37 = Staff((Inch(0.5), Inch(1.5)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_37 = InvisibleClef(Unit(0), staff_37, 'treble')
    tremolo_rank_1(staff_37, y)

    staff_38 = Staff((Inch(2), Inch(1.5)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_38 = InvisibleClef(Unit(0), staff_38, 'treble')
    tremolo_rank_2(staff_38, y)

    staff_39 = Staff((Inch(3.5), Inch(1.5)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_39 = InvisibleClef(Unit(0), staff_39, 'treble')
    tremolo_rank_3(staff_39, y)

    staff_40 = Staff((Inch(5), Inch(1.5)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_40 = InvisibleClef(Unit(0), staff_40, 'treble')
    tremolo_rank_4(staff_40, y)

    staff_41 = Staff((Inch(0.5), Inch(3)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_41 = InvisibleClef(Unit(0), staff_41, 'treble')
    adv_harm_rank_1(staff_41, y)

    staff_42 = Staff((Inch(2), Inch(3)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_42 = InvisibleClef(Unit(0), staff_42, 'treble')
    adv_harm_rank_2(staff_42, y)

    staff_43 = Staff((Inch(3.5), Inch(3)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_43 = InvisibleClef(Unit(0), staff_43, 'treble')
    adv_harm_rank_3(staff_43, y)

    staff_44 = Staff((Inch(5), Inch(3)), parent=neoscore.document.pages[1], length=Inch(1))
    clef_44 = InvisibleClef(Unit(0), staff_44, 'treble')
    adv_harm_rank_4(staff_44, y)

    neoscore.show()
