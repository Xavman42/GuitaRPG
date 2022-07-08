from neoscore.common import *
import numpy as np
import time
import pathlib
import threading
#import keyboard
import random

framerate = 60
class mover:
    score_x = Unit(0) #Score does not rotate
    score_x_ini = Unit(0) #Point around which rotation occurs

    def __init__(self, xpos, ypos, rot, image_path, scale=1.0):
        self.xpos = xpos
        self.xpos_ref = xpos
        self.xpos_ini = xpos
        self.ypos = ypos
        self.ypos_ref = ypos
        self.ypos_ini = ypos
        self.rot = rot
        self.rot_ref = rot
        self.rot_ini = rot
        self.image_path = image_path
        self.rendering = True
        self.scale = scale

    def instantiate_mover(self):
        global reticle
        if type(self.image_path) is str:
            self.obj = Text((self.xpos,self.ypos),reticle,self.image_path,rotation = self.rot)
        else:
            self.obj = Image((self.xpos,self.ypos),reticle,self.image_path,rotation = self.rot, scale = self.scale)

    def make_invisible(self):
        self.obj.remove()
        self.rendering = False

    def prep_object(self):
        self.xpos_ini = self.xpos
        self.ypos_ini = self.ypos
        self.xpos = self.xpos - self.score_x_ini
        self.rot_ini = self.rot

    @classmethod
    def score_shift(cls,t,distance,duration):
        cls.score_x = cls.score_x_ini + Unit(t*distance/duration)

    @classmethod
    def confirm_score_shift(cls,distance):
        cls.score_x = cls.score_x_ini + Unit(distance)

    def obj_forward(self,t):
        self.xpos = self.xpos_ini - self.score_x
        if self.rendering:
            self.obj.x = self.xpos
            self.obj.y = self.ypos

    def confirm_obj_forward(self):
        self.xpos = self.xpos_ini - self.score_x
        if self.rendering:
            self.obj.x = self.xpos
            self.obj.y = self.ypos

    def obj_rotate(self,t,degrees,rot_time):
        self.rot = self.rot_ini + t*degrees/rot_time
        self.xpos = (self.xpos_ini * np.cos(t*np.deg2rad(degrees)/rot_time)-self.ypos_ini * np.sin(t*np.deg2rad(degrees)/rot_time))
        self.ypos = (self.ypos_ini * np.cos(t*np.deg2rad(degrees)/rot_time)+self.xpos_ini * np.sin(t*np.deg2rad(degrees)/rot_time))
        if self.rendering:
            self.obj.rotation = self.rot
            self.obj.x = self.xpos
            self.obj.y = self.ypos

    def confirm_obj_rotate(self,degrees):
        self.rot = self.rot_ini + degrees
        self.xpos = (self.xpos_ini * np.cos(np.deg2rad(degrees))-self.ypos_ini * np.sin(np.deg2rad(degrees)))
        self.ypos = (self.ypos_ini * np.cos(np.deg2rad(degrees))+self.xpos_ini * np.sin(np.deg2rad(degrees)))
        if self.rendering:
            self.obj.rotation = self.rot
            self.obj.x = self.xpos
            self.obj.y = self.ypos

class tree_branch:
    E_scrape_exp = 1
    E_scrape_rank = 1
    perc_exp = 1
    perc_rank = 1
    tamb_exp = 1
    tamb_rank = 1

    def __init__(self, image_path = "image_path", skill="skill_name", rank=0, exp=1, max_exp = 5, min_exp = 1):
        self.skill = skill
        self.rank = rank
        self.exp = exp
        self.image_path = image_path
        self.max_exp = max_exp
        self.scale = 0.4
        self.min_exp = min_exp

    def exp_gain(self, gain=1):
        self.exp = self.exp + gain
        if self.exp > self.max_exp:
            self.exp = self.min_exp

    @classmethod
    def E_scrape_exp_gain(cls,gain=1):
        global skills
        global scrape_HUD
        temp_exp = 1
        temp_max_exp = 5
        temp_min_exp = 1
        cls.E_scrape_exp = cls.E_scrape_exp + gain
        if cls.E_scrape_exp > 4:
            cls.E_scrape_exp = 1
            cls.E_scrape_rank = cls.E_scrape_rank + 1
            if(cls.E_scrape_rank == 2):
                skills = np.append(skills,tree_branch(skill = "E_scrape_rank_2", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
                scrape_HUD.text = "Scrape "+ str(tree_branch.E_scrape_rank)
            elif(cls.E_scrape_rank == 3):
                skills = np.append(skills,tree_branch(skill = "E_scrape_rank_3", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
                scrape_HUD.text = "Scrape "+ str(tree_branch.E_scrape_rank)
            elif(cls.E_scrape_rank == 4):
                skills = np.append(skills,tree_branch(skill = "E_scrape_rank_4", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
                scrape_HUD.text = "Scrape "+ str(tree_branch.E_scrape_rank)
            elif(cls.E_scrape_rank == 5):
                skills = np.append(skills,tree_branch(skill = "E_scrape_rank_5", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
                scrape_HUD.text = "Scrape max"
            else:scrape_HUD.text = "Scrape max"

    @classmethod
    def perc_exp_gain(cls,gain=1):
        global skills
        global perc_HUD
        temp_exp = 6
        temp_max_exp = 12
        temp_min_exp = 6
        cls.perc_exp = cls.perc_exp + gain
        if cls.perc_exp > 5:
            cls.perc_exp = 2
            cls.perc_rank = cls.perc_rank + 1
            perc_HUD.text = "Perc "+ str(tree_branch.perc_rank)
            if(cls.perc_rank == 2):
                skills = np.append(skills,tree_branch(skill = "perc_rank_2", image_path = perc_image_2, exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
                perc_HUD.text = "Perc "+ str(tree_branch.perc_rank)
            elif(cls.perc_rank == 3):
                skills = np.append(skills,tree_branch(skill = "perc_rank_3", image_path = perc_image_3, exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
                perc_HUD.text = "Perc max"
            else:perc_HUD.text = "Perc max"

    @classmethod
    def tamb_exp_gain(cls,gain=1):
        global skills
        global tamb_HUD
        temp_exp = 10
        temp_max_exp = 20
        temp_min_exp = 10
        cls.tamb_exp = cls.tamb_exp + gain
        if cls.tamb_exp > 4:
            cls.tamb_exp = 1
            cls.tamb_rank = cls.tamb_rank + 1
            tamb_HUD.text = "Tamb "+ str(tree_branch.tamb_rank)
            if(cls.tamb_rank == 2):
                skills = np.append(skills,tree_branch(skill = "tamb_rank_2", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
                tamb_HUD.text = "Tamb max"
            else:tamb_HUD.text = "Tamb max"

    def generate_cell(self, loc):
        def E_scrape_rank_1(loc):
            start = Chordrest(staff.unit(loc), staff, ["e'"],(1,4), table=notehead_tables.X)
            end = Chordrest(staff.unit(loc+8), staff, ["e"],(1,4), table=notehead_tables.X)
            RepeatingMusicTextLine((staff.unit(2),ZERO), start.highest_notehead,
                (staff.unit(0), ZERO), end.highest_notehead,
                "wiggleTrillFastest", None)
            string_6 = Image((staff.unit(2+loc)-Unit(20),Unit(-80)),staff,sul_6, scale=0.7)
        def E_scrape_rank_2(loc):
            start_1 = Chordrest(staff.unit(loc), staff, ["e"],(1,4), table=notehead_tables.X)
            end_1 = Chordrest(staff.unit(loc+3), staff, ["e'"],(1,4), table=notehead_tables.X)
            RepeatingMusicTextLine((staff.unit(2),ZERO), start_1.highest_notehead,
                (staff.unit(0), ZERO), end_1.highest_notehead,
                "wiggleTrillFastest", None)
            start_2 = Chordrest(staff.unit(loc+5), staff, ["e"],(1,4), table=notehead_tables.X)
            end_2 = Chordrest(staff.unit(loc+8), staff, ["e'"],(1,4), table=notehead_tables.X)
            RepeatingMusicTextLine((staff.unit(2),ZERO), start_2.highest_notehead,
                (staff.unit(0), ZERO), end_2.highest_notehead,
                "wiggleTrillFastest", None)
            string_6 = Image((staff.unit(2+loc)-Unit(20),Unit(-80)),staff,sul_6, scale=0.7)
        def E_scrape_rank_3(loc):
            start = Chordrest(staff.unit(loc), staff, ["e"],(1,4), table=notehead_tables.X)
            middle = Chordrest(staff.unit(loc+3.5), staff, ["e'"],(1,4), table=notehead_tables.X)
            end = Chordrest(staff.unit(loc+7), staff, ["e"],(1,4), table=notehead_tables.X)
            RepeatingMusicTextLine((staff.unit(2),ZERO), start.highest_notehead,
                (staff.unit(0), ZERO), middle.highest_notehead,
                "wiggleTrillFastest", None)
            RepeatingMusicTextLine((staff.unit(2),ZERO), middle.highest_notehead,
                (staff.unit(0), ZERO), end.highest_notehead,
                "wiggleTrillFastest", None)
            string_6 = Image((staff.unit(2+loc)-Unit(20),Unit(-80)),staff,sul_6, scale=0.7)
        def E_scrape_rank_4(loc):
            start_1 = Chordrest(staff.unit(loc), staff, ["e"],(1,4), table=notehead_tables.X)
            end_1 = Chordrest(staff.unit(loc+2), staff, ["e'"],(1,4), table=notehead_tables.X)
            RepeatingMusicTextLine((staff.unit(2),ZERO), start_1.highest_notehead,
                (staff.unit(0), ZERO), end_1.highest_notehead,
                "wiggleTrillFastest", None)
            start_2 = Chordrest(staff.unit(loc+4), staff, ["e"],(1,4), table=notehead_tables.X)
            end_2 = Chordrest(staff.unit(loc+6), staff, ["e'"],(1,4), table=notehead_tables.X)
            RepeatingMusicTextLine((staff.unit(2),ZERO), start_2.highest_notehead,
                (staff.unit(0), ZERO), end_2.highest_notehead,
                "wiggleTrillFastest", None)
            string_6 = Image((staff.unit(2+loc)-Unit(20),Unit(-80)),staff,sul_6, scale=0.7)
        def E_scrape_rank_5(loc):
            start_1 = Chordrest(staff.unit(loc), staff, ["e"],(1,4), table=notehead_tables.X)
            middle_1 = Chordrest(staff.unit(loc+2), staff, ["e'"],(1,4), table=notehead_tables.X)
            middle_2 = Chordrest(staff.unit(loc+6), staff, ["e"],(1,4), table=notehead_tables.X)
            end_1 = Chordrest(staff.unit(loc+8), staff, ["e'"],(1,4), table=notehead_tables.X)
            RepeatingMusicTextLine((staff.unit(2),ZERO), start_1.highest_notehead,
                (staff.unit(0), ZERO), middle_1.highest_notehead,
                "wiggleTrillFastest", None)
            RepeatingMusicTextLine((staff.unit(2),ZERO), middle_1.highest_notehead,
                (staff.unit(0), ZERO), middle_2.highest_notehead,
                "wiggleTrillFastest", None)
            RepeatingMusicTextLine((staff.unit(2),ZERO), middle_2.highest_notehead,
                (staff.unit(0), ZERO), end_1.highest_notehead,
                "wiggleTrillFastest", None)
            string_6 = Image((staff.unit(2+loc)-Unit(20),Unit(-80)),staff,sul_6, scale=0.7)

        def perc_rank_1(loc):
            Image((Unit(staff.unit(loc)),Unit(-80)), staff, self.image_path, scale=self.scale)
        def perc_rank_2(loc):
            Image((Unit(staff.unit(loc)),Unit(-80)), staff, self.image_path, scale=self.scale)
        def perc_rank_3(loc):
            Image((Unit(staff.unit(loc)),Unit(-80)), staff, self.image_path, scale=self.scale)

        def tamb_rank_1(loc):
            note_1 = Chordrest(staff.unit(loc+4), staff, ["g,"],(1,4), table=notehead_tables.TRIANGLE_UP)
        def tamb_rank_2(loc):
            note_1 = Chordrest(staff.unit(loc+4), staff, ["g,"],(1,8), table=notehead_tables.TRIANGLE_UP)
            note_2 = Chordrest(staff.unit(loc+8), staff, ["g,"],(1,8), table=notehead_tables.TRIANGLE_UP)

        self.exp_gain()

        if self.skill == "E_scrape_rank_1":E_scrape_rank_1(loc),tree_branch.E_scrape_exp_gain()
        elif self.skill == "E_scrape_rank_2":E_scrape_rank_2(loc),tree_branch.E_scrape_exp_gain()
        elif self.skill == "E_scrape_rank_3":E_scrape_rank_3(loc),tree_branch.E_scrape_exp_gain()
        elif self.skill == "E_scrape_rank_4":E_scrape_rank_4(loc),tree_branch.E_scrape_exp_gain()
        elif self.skill == "E_scrape_rank_5":E_scrape_rank_5(loc),tree_branch.E_scrape_exp_gain()
        elif self.skill == "perc_rank_1":perc_rank_1(loc),tree_branch.perc_exp_gain()
        elif self.skill == "perc_rank_2":perc_rank_2(loc),tree_branch.perc_exp_gain()
        elif self.skill == "perc_rank_3":perc_rank_3(loc),tree_branch.perc_exp_gain()
        elif self.skill == "tamb_rank_1":tamb_rank_1(loc),tree_branch.tamb_exp_gain()
        elif self.skill == "tamb_rank_2":tamb_rank_2(loc),tree_branch.tamb_exp_gain()
        else: print("not a skill")

#class particle:
    #particles are sent to the SuperCollider!
#    def __init__(self, sound = "beep"):
#        self.sound = sound

#    @classmethod
#    def generate_marker(self, loc, image_path = "star_1"):
#        Image((Unit(staff.unit(loc)),Unit(-90)), staff, star_1)

def make_movers():
    global movers
    for i in range(movers.size):
        movers[i].instantiate_mover()

def render_area():
    while True:
        #check_bounds()
        total_time = float(time.time())-program_start_time
        time_text.text =  ("{:#.2f}"+" seconds").format(total_time)
        time.sleep(0.1)

def new_move():
    global movers
    temp = int(time.time())
    for i in range(movers.size):
        movers[i].prep_object()
    return temp

def static(time:float):
    pass

def go_forward(dur,dist,region):
    empty_cells()
    generate_staff_contents()
    def forward(t):
        global movers
        mover.score_shift(t,dist,dur)
        staff.x = -mover.score_x
        for i in range(movers.size):
            movers[i].obj_forward(t)
    def refresh_func_forward(time:float):
        global movers
        global start_time
        t = time-start_time
        forward(t)
        if t >=dur:
            mover.confirm_score_shift(dist)
            for i in range(movers.size):
                movers[i].confirm_obj_forward()
            #check_bounds()
            start_time = new_move()
            sequence()
    neoscore.set_refresh_func(refresh_func_forward, framerate)

def go_rotate(rot_time,degrees):
    empty_cells()
    def rotate(t,degrees,rot_time):
        global movers
        for i in range(movers.size):
            movers[i].obj_rotate(t,degrees,rot_time)
    def refresh_func_rot(time:float):
        global movers
        global start_time
        t = time-start_time
        rotate(t,degrees,rot_time)
        if t >=rot_time:
            for i in range(movers.size):
                movers[i].confirm_obj_rotate(degrees)
            #check_bounds()
            start_time = new_move()
            sequence()
    neoscore.set_refresh_func(refresh_func_rot, framerate)

def sequence():
    global region
    global skills
    global scrape_HUD, perc_HUD, tamb_HUD
    unit_length = 1000
    rate = 15
    rot_rate = 1
    if region == "A0":
        go_forward(rate, unit_length, region) #format(duration(s), distance(px))
        region = "A1"
    elif region == "A1":
        go_forward(rate, unit_length, region)
        region = "A2"
    elif region == "A2":
        go_forward(rate, unit_length, region)
        region = "A3"
    elif region == "A3":
        scrape_HUD = Text((Unit(450), Unit(-450)), None, "Scrape "+ str(tree_branch.E_scrape_rank))
        skills = np.append(skills,tree_branch(skill = "E_scrape_rank_1"))
        go_forward(rate, unit_length, region)
        region = "A4"
    elif region == "A4":
        go_forward(rate, unit_length, region)
        region = "A4_rot"
    elif region == "A4_rot":
        go_rotate(rot_rate, 30)
        region = "A5_to_B1"
    elif region == "A5_to_B1":
        go_forward(rate, unit_length, region)
        region = "A5_to_B1_rot"
    elif region == "A5_to_B1_rot":
        go_rotate(rot_rate, 60)
        region = "B1"
    elif region == "B1":
        perc_HUD = Text((Unit(390), Unit(-450)), None, "Perc "+ str(tree_branch.perc_rank))
        skills = np.append(skills,tree_branch(skill = "perc_rank_1", image_path = perc_image_1, exp = 6, max_exp = 12, min_exp = 6))
        go_forward(rate, unit_length, region)
        region = "B1_rot"
    elif region == "B1_rot":
        go_rotate(rot_rate, -90)
        region = "B2"
    elif region == "B2":
        go_forward(rate, unit_length, region)
        region = "B2_rot"
    elif region == "B2_rot":
        go_rotate(rot_rate, -90)
        region = "B3"
    elif region == "B3":
        go_forward(rate, unit_length, region)
        region = "B3_rot_cw"
    elif region == "B3_rot_cw":
        go_rotate(rot_rate, -90)
        region = "B4"
    elif region == "B4":
        go_forward(rate, unit_length, region)
        region = "B4_rot"
    elif region == "B4_rot":
        go_rotate(rot_rate, -90)
        region = "B1(2)"
    elif region == "B1(2)":
        go_forward(rate, unit_length, region)
        region = "B1_rot(2)"
    elif region == "B1_rot(2)":
        go_rotate(rot_rate, -90)
        region = "B2(2)"
    elif region == "B2(2)":
        go_forward(rate, unit_length, region)
        region = "B2_rot(2)"
    elif region == "B2_rot(2)":
        go_rotate(rot_rate, -90)
        region = "B3(2)"
    elif region == "B3(2)":
        go_forward(rate, unit_length, region)
        region = "B3_rot_straight"
    elif region == "B3_rot_straight":
        #go_rotate(rot_rate, 0)
        region = "B3_to_C2"
        sequence()
    elif region == "B3_to_C2":
        go_forward(rate, unit_length, region)
        region = "B3_to_C2_rot_straight"
    elif region == "B3_to_C2_rot_straight":
        #go_rotate(rot_rate,0)
        region = "C2"
        sequence()
    elif region == "C2":
        tamb_HUD = Text((Unit(320), Unit(-450)), None, "Tamb "+ str(tree_branch.tamb_rank))
        skills = np.append(skills,tree_branch(skill = "tamb_rank_1", exp=10, max_exp=20, min_exp=10))
        go_forward(rate, unit_length, region)
        region = "C2_rot"
    elif region == "C2_rot":
        go_rotate(rot_rate, -90)
        region = "C3"
    elif region == "C3":
        go_forward(rate, unit_length, region)
        region = "C3_rot"
    elif region == "C3_rot":
        go_rotate(rot_rate, -90)
        region = "C4"
    elif region == "C4":
        go_forward(rate, unit_length, region)
        region = "C4_rot"
    elif region == "C4_rot":
        go_rotate(rot_rate, -90)
        region = "C1"
    elif region == "C1":
        go_forward(rate, unit_length, region)
        region = "C1_rot_ccw"
    elif region == "C1_rot_ccw":
        go_rotate(rot_rate, 30)
        region = "C1_to_D1"
    elif region == "C1_to_D1":
        go_forward(rate, unit_length, region)
        region = "C1_to_D1_rot"
    elif region == "C1_to_D1_rot":
        go_rotate(rot_rate, -30)
        region = "D1"
    elif region == "D1":
        go_forward(rate, unit_length, region)
        region = "D2"
    else: neoscore.set_refresh_func(static)
    return region

def empty_cells():
    global cells
    global staff
    staff.remove()
    staff = Staff((window_center_x-Unit(20),window_center_y), None, Unit(500), line_spacing=Unit(20), pen = (Pen(pattern = PenPattern.INVISIBLE)))
    invisible_clef = Clef(Unit(-1000), staff, 'treble', pen = (Pen(pattern = PenPattern.INVISIBLE)))

def generate_staff_contents():
    global cells
    global skills
    global staff
    empty_cells()
    cells = np.array([])
    weights = np.array([])
    particles = np.array([])
    number_of_cells = 4
    skill_indicies = np.arange(skills.size)
    #for i in range(number_of_cells):
    #    particles = np.append(particles,particle.generate_marker(5+i*10))
    for i in range(skills.size):
        weights = np.append(weights,skills[i].exp)
    if weights.size > 0:
        weighted_list = random.choices(skill_indicies, weights, k=number_of_cells)
        for i in range(number_of_cells):
            skills[weighted_list[i]].exp_gain
            cells = np.append(cells,skills[weighted_list[i]].generate_cell(5+i*10))

def make_map():
    global movers
    unit_length = 1000

    for i in range(5):
        movers = np.append(movers,mover(Unit(0+(unit_length*i)),Unit(0),0,staff_1))

    movers = np.append(movers,mover(Unit(40),Unit(-100),0,"Hello, and welcome to the tech demo for GuitaRPG!"))
    movers = np.append(movers,mover(Unit(340),Unit(-100),0,"This piece is written for classical guitar, and SuperCollider is used to generate additional sounds in real-time (not yet implemented)"))
    movers = np.append(movers,mover(Unit(1100),Unit(-100),0,"The guitarist reads the staff, playing material as it passes through the reticle, while calls to SuperCollider are represented by shapes above the staff"))
    #movers = np.append(movers,mover(Unit(1200),Unit(0),0,guit_cell_1))

    movers = np.append(movers,mover(Unit(1950),Unit(-100),0,"In this demo, there are three types of materials which will appear: scraping along the E string, various percussive effects, and tambura"))
    movers = np.append(movers,mover(Unit(2700),Unit(-100),0,"Let's now begin with the first of the sounds, the scrape along the E string"))

    movers = np.append(movers,mover(Unit(3150),Unit(-100),0,"The more times a type of material appears, the more variations of that material begin to appear. The rank of each material-type is shown in the upper-right corner"))


    movers = np.append(movers,mover(Unit(4150),Unit(-100),0,"The performer interacts with the score to choose what direction to go (this is automated for now)"))

    movers = np.append(movers,mover(Unit(5000),Unit(-100),-30,"Now we are moving to a new region of the score to learn a new skill!"))
    movers = np.append(movers,mover(Unit(5*unit_length),Unit(0),-30,staff_1))
    movers = np.append(movers,mover(Unit(5*unit_length),Unit(0),30,staff_1))
    #movers = np.append(movers,mover(Unit(5*unit_length-100),Unit(-100),0,disk_1,0.5))

    reg_2_x = 5*unit_length+unit_length*np.cos(np.deg2rad(-30))
    movers = np.append(movers,mover(Unit(reg_2_x),Unit(unit_length*np.sin(np.deg2rad(-30))),-90,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x-100),Unit(unit_length*np.sin(np.deg2rad(-30))-200),-90,"Different percussive effects are pictographically represented on the score"))
    movers = np.append(movers,mover(Unit(reg_2_x),Unit(-unit_length+unit_length*np.sin(np.deg2rad(-30))),0,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x+200),Unit(-unit_length+unit_length*np.sin(np.deg2rad(-30))-100),0,"In the final product, there will be many more variations of these symbols"))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length),Unit(-unit_length+unit_length*np.sin(np.deg2rad(-30))),90,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length+100),Unit(-unit_length+unit_length*np.sin(np.deg2rad(-30))+200),90,"The player may choose to stay in a region as long as they like to further explore the sound of that region"))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length),Unit(unit_length*np.sin(np.deg2rad(-30))),180,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length-100),Unit(unit_length*np.sin(np.deg2rad(-30))+100),180,"In this example, the player decides to stay in the percussive region a little longer. In a moment you will see familiar text"))

    movers = np.append(movers,mover(Unit(reg_2_x+unit_length),Unit(unit_length*np.sin(np.deg2rad(-30))),90,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length+100),Unit(unit_length*np.sin(np.deg2rad(-30))+200),90,"Now we move to the next region. Here we focus on sounds using Tambura"))


    movers = np.append(movers,mover(Unit(reg_2_x),Unit(-unit_length*np.sin(np.deg2rad(-30))),0,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x+200),Unit(-unit_length*np.sin(np.deg2rad(-30))-100),0,"We're approaching the end of the demo now!"))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length),Unit(-unit_length*np.sin(np.deg2rad(-30))),90,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length+100),Unit(-unit_length*np.sin(np.deg2rad(-30))+100),90,"In each region, the effects chain used to process the sound of the guitar changes as well, helping to make the techniques have their own contextual meaning"))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length),Unit(unit_length-unit_length*np.sin(np.deg2rad(-30))),180,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length-200),Unit(unit_length-unit_length*np.sin(np.deg2rad(-30))+100),180,"The full score will have many more regions, skills, and variations"))
    movers = np.append(movers,mover(Unit(reg_2_x),Unit(unit_length-unit_length*np.sin(np.deg2rad(-30))),270,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x-100),Unit(unit_length-unit_length*np.sin(np.deg2rad(-30))-200),270,"The current region determines what technique the performer is most likely to encounter"))


    movers = np.append(movers,mover(Unit(reg_2_x+unit_length),Unit(unit_length*np.sin(np.deg2rad(-30))),30,staff_1))
    movers = np.append(movers,mover(Unit(reg_2_x+unit_length),Unit(-unit_length*np.sin(np.deg2rad(-30))),-30,staff_1))

    reg_3_x = reg_2_x+unit_length+unit_length*np.cos(np.deg2rad(30))
    movers = np.append(movers,mover(Unit(reg_3_x+200),Unit(-200),0,"We've reached the end of the tech demo! Bye bye"))
    movers = np.append(movers,mover(Unit(reg_3_x),Unit(0),0,staff_1))

def make_HUD():
    global reticle, time_text
    reticle_path = Path((window_center_x+Unit(-10),window_center_y+Unit(110)),None, Brush.no_brush(), pen = Pen("000000",Unit(4), PenPattern.DOT))
    reticle_path.line_to(Unit(0),Unit(-140))
    reticle_path.line_to(Unit(20),Unit(-140))
    reticle_path.line_to(Unit(20),Unit(0))
    reticle_path.line_to(Unit(0),Unit(0))
    reticle = Text((window_center_x,window_center_y), None, " ")
    staff_for_clef = Staff((window_center_x-Unit(20),window_center_y), None, Unit(500), line_spacing=Unit(20), pen = (Pen(pattern = PenPattern.INVISIBLE)))
    clef = Clef(ZERO, staff_for_clef, 'treble')
    time_text = Text((Unit(-100), Unit(-150)), None, "0.00")

def main():
    global movers
    global start_time
    global staff
    global cells
    global region
    global skills
    global staff
    global window_center_x, window_center_y

    region = "A0"

    neoscore.setup()
    window_center_x = Unit(0)
    window_center_y = Unit(-300)

    staff = Staff((window_center_x-Unit(20),window_center_y), None, Unit(500), line_spacing=Unit(20))
    invisible_clef = Clef(Unit(-1000), staff, 'treble', pen = (Pen(pattern = PenPattern.INVISIBLE)))
    direction = Text((window_center_x+Unit(300),window_center_y+Unit(200)),None,text ="Up")

    movers = np.array([])
    cells = np.array([])
    skills = np.array([])

    make_map()
    make_HUD()

    make_movers()
    start_time = new_move()

    render_thread = threading.Thread(target=render_area)
    render_thread.start()

    sequence()
    neoscore.set_viewport_center_pos((window_center_x+Unit(200),window_center_y))
    neoscore.set_viewport_scale(2)
    neoscore.show(display_page_geometry=True, auto_viewport_interaction_enabled=True, min_window_size=(1280,720), max_window_size=(1280,720))

if __name__ == '__main__':
    perc_image_1 = pathlib.Path("Assets/perc_images")/"perc_image_1.png"
    perc_image_2 = pathlib.Path("Assets/perc_images")/"perc_image_2.png"
    perc_image_3 = pathlib.Path("Assets/perc_images")/"perc_image_3.png"
    test_image_1 = pathlib.Path("Assets")/"test_image_1"
    test_image_2 = pathlib.Path("Assets")/"test_image_2"
    test_image_3 = pathlib.Path("Assets")/"test_image_3"
    test_image_4 = pathlib.Path("Assets")/"test_image_4"
    test_image_5 = pathlib.Path("Assets")/"test_image_5"
    staff_1 = pathlib.Path("Assets")/"staff_1000px.png"
    guit_cell_1 = pathlib.Path("Assets")/"squiggle_1.png"
    star_1 = pathlib.Path("Assets")/"star_1.png"
    disk_1 = pathlib.Path("Assets")/"disk.png"
    sul_6 = pathlib.Path("Assets")/"sul_6.png"
    #input("press enter to begin")
    program_start_time = int(time.time())
    main()
