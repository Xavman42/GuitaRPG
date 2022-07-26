from neoscore.common import *
import pyOSC3
import numpy as np
import time
import pathlib
import random
import os

#If there are any memory leak issues, the framerate can be lowered to mitigate the issue slightly.
#I have only ever experienced a memory leak on a Windows 10 laptop.
#For better performance in the future, I will convert many of the calculations to lookup table searches instead. A consistent 60Hz shouldn't be an issue for this project. 
framerate = 60

class static_element:
    #This class describes the location of every static element in the window. All visible staff-lines staff lines have these properties.
    def __init__(self, xpos, ypos, rot, image_or_string, scale=1.0):
        self.xpos = xpos
        self.xpos_ini = xpos
        self.ypos = ypos
        self.ypos_ini = ypos
        self.rot = rot
        self.rot_ini = rot
        self.image_or_string = image_or_string
        self.scale = scale
        if type(self.image_or_string) is str:
            self.obj = Text((self.xpos,self.ypos),None, self.image_or_string,rotation=self.rot)
        else:
            self.obj = Image((self.xpos,self.ypos),None,self.image_or_string, rotation=self.rot,scale=self.scale)

    
    def obj_rotate(self,t,degrees,rot_time,x_point,y_point):
        #The viewport only moves horizontally. To make the viewport seem like it is rotating, I rotate all static elements about a single point.
        #I do this because there is no way currently to use the neoscore staff object off-axis. I should go and add that feature sometime. 
        self.obj.rotation = self.rot_ini + t*degrees/rot_time
        self.obj.x = ((self.xpos_ini-x_point) * np.cos(t*np.deg2rad(degrees)/rot_time)-(self.ypos_ini-y_point)*np.sin(t*np.deg2rad(degrees)/rot_time))+x_point
        self.obj.y = ((self.ypos_ini-y_point)*np.cos(t*np.deg2rad(degrees)/rot_time)+(self.xpos_ini-x_point)*np.sin(t*np.deg2rad(degrees)/rot_time))+y_point

    def confirm_obj_rotate(self,degrees,x_point,y_point):
        #The time-dependent rotation is sometimes innacurate. This corrects animation glitches.
        self.obj.rotation = self.rot_ini + degrees
        self.obj.x = ((self.xpos_ini-x_point) * np.cos(np.deg2rad(degrees))-(self.ypos_ini-y_point)*np.sin(np.deg2rad(degrees)))+x_point
        self.obj.y = ((self.ypos_ini-y_point)*np.cos(np.deg2rad(degrees))+(self.xpos_ini-x_point)*np.sin(np.deg2rad(degrees)))+y_point
        self.rot_ini = self.obj.rotation
        self.xpos_ini = self.obj.x
        self.ypos_ini = self.obj.y

class tree_branch:
    #This class maintains all information about skill experience. 
    #The rank and experience of each skills is stored at the class level.
    #The class also handles the generation of materials for the performer to play.
    E_scrape_exp = 1
    E_scrape_rank = 0
    perc_exp = 1
    perc_rank = 0
    tamb_exp = 1
    tamb_rank = 0

    def __init__(self, image_path = "image_path", skill="skill_name", rank=0, exp=1, max_exp = 5, min_exp = 1):
        self.skill = skill
        self.rank = rank
        self.exp = exp
        self.image_path = image_path
        self.max_exp = max_exp
        self.scale = 0.4
        self.min_exp = min_exp

    def exp_gain(self, gain=1):
        #This increases the experience level of a skill and resets the experience after a certain number is reached.
        #This experience level affects the likelyhood of a particular skill appearing.
        self.exp = self.exp + gain
        if self.exp > self.max_exp:
            self.exp = self.min_exp

    @classmethod
    def E_scrape_exp_gain(cls,gain=1):
        global skills
        temp_exp = 5
        temp_max_exp = 5
        temp_min_exp = 1
        E_scrape_max_rank = 5
        cls.E_scrape_exp = cls.E_scrape_exp + gain
        if cls.E_scrape_exp > 4:
            cls.E_scrape_exp = 1
            if (cls.E_scrape_rank < E_scrape_max_rank): cls.E_scrape_rank = cls.E_scrape_rank + 1
            if(cls.E_scrape_rank == 2):
                skills = np.append(skills,tree_branch(skill = "E_scrape_rank_2", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
            elif(cls.E_scrape_rank == 3):
                skills = np.append(skills,tree_branch(skill = "E_scrape_rank_3", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
            elif(cls.E_scrape_rank == 4):
                skills = np.append(skills,tree_branch(skill = "E_scrape_rank_4", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
            elif(cls.E_scrape_rank == 5):
                skills = np.append(skills,tree_branch(skill = "E_scrape_rank_5", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))

    @classmethod
    def perc_exp_gain(cls,gain=1):
        global skills
        temp_exp = 15
        temp_max_exp = 16
        temp_min_exp = 6
        perc_max_rank = 3
        cls.perc_exp = cls.perc_exp + gain
        if cls.perc_exp > 5:
            cls.perc_exp = 2
            if (cls.perc_rank < perc_max_rank): cls.perc_rank = cls.perc_rank + 1
            if(cls.perc_rank == 2):
                skills = np.append(skills,tree_branch(skill = "perc_rank_2", image_path = perc_image[1], exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))
            elif(cls.perc_rank == 3):
                skills = np.append(skills,tree_branch(skill = "perc_rank_3", image_path = perc_image[2], exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))

    @classmethod
    def tamb_exp_gain(cls,gain=1):
        global skills
        temp_exp = 30
        temp_max_exp = 31
        temp_min_exp = 18
        tamb_max_rank = 2
        cls.tamb_exp = cls.tamb_exp + gain
        if cls.tamb_exp > 4:
            cls.tamb_exp = 1
            if (cls.tamb_rank < tamb_max_rank): cls.tamb_rank = cls.tamb_rank + 1
            if(cls.tamb_rank == 2):
                skills = np.append(skills,tree_branch(skill = "tamb_rank_2", exp = temp_exp, max_exp = temp_max_exp, min_exp = temp_min_exp))

    def generate_cell(self, loc):
        #This is an inelegant way to select and generate materials which the performer plays.
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

        def star(loc):
            Image((Unit(staff.unit(loc)),Unit(-150)), staff, self.image_path, scale=self.scale)

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
        elif self.skill == "star":star(loc)
        else: print("not a skill")

def make_render_area():
    # Scene bounding rectangle. This ensures translation works as desired.
    bound_val = 9999
    Path.rect((Mm(-bound_val), Mm(-bound_val)), None, Mm(2*bound_val), Mm(2*bound_val),
              Brush.no_brush(), "#ff00ff55")

def make_map(static_elements):
    #This manually places every static element in the window.
    #This should be a generative process in the future.
    unit_length = 1000

    for i in range(4):
        static_elements = np.append(static_elements,static_element(Unit(0+(unit_length*i)),Unit(0),0,staff_1))

    static_elements = np.append(static_elements,static_element(Unit(0+(unit_length*4)),Unit(-500),0,staff_30_junction))

    static_elements = np.append(static_elements,static_element(Unit(0),Unit(-125),0,"PRESS ANY KEY TO BEGIN"))
    static_elements = np.append(static_elements,static_element(Unit(40),Unit(-100),0,"Hello, and welcome to the tech demo for GuitaRPG!"))
    static_elements = np.append(static_elements,static_element(Unit(340),Unit(-100),0,"This piece is written for classical guitar, and SuperCollider is used to generate additional sounds in real-time"))
    static_elements = np.append(static_elements,static_element(Unit(1100),Unit(-100),0,"The guitarist reads the staff, playing material as it passes through the reticle, while calls to SuperCollider are represented by stars above the staff"))
    #static_elements = np.append(static_elements,static_element(Unit(1200),Unit(0),0,guit_cell_1))

    static_elements = np.append(static_elements,static_element(Unit(1950),Unit(-100),0,"In this demo, there are three types of materials which will appear: scraping along the E string, various percussive effects, and tambura"))
    static_elements = np.append(static_elements,static_element(Unit(2700),Unit(-100),0,"Let's now begin with the first of the sounds, the scrape along the E string"))

    static_elements = np.append(static_elements,static_element(Unit(3150),Unit(-100),0,"The more times a type of material appears, the more variations of that material begin to appear. The rank of each material-type is shown in the upper-right corner"))


    static_elements = np.append(static_elements,static_element(Unit(4150),Unit(-100),0,"The performer interacts with the score to choose what direction to go (this is automated for now)"))

    static_elements = np.append(static_elements,static_element(Unit(5000),Unit(-100),-30,"Now we are moving to a new region of the score to learn a new skill!"))
    static_elements = np.append(static_elements,static_element(Unit(4800),Unit(-100),-30, perc_signpost, scale = 0.25))
    static_elements = np.append(static_elements,static_element(Unit(4800),Unit(100),30, tamb_signpost, scale = 0.25))


    reg_2_x = 5*unit_length+unit_length*np.cos(np.deg2rad(-30))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x),Unit(unit_length*np.sin(np.deg2rad(-30))),-90,staff_1))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x),Unit(unit_length*np.sin(np.deg2rad(-30))),-30,staff_angle_60))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x-100),Unit(unit_length*np.sin(np.deg2rad(-30))-200),-90,"Different percussive effects are pictographically represented on the score"))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x),Unit(-unit_length+unit_length*np.sin(np.deg2rad(-30))),0,staff_1))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+200),Unit(-unit_length+unit_length*np.sin(np.deg2rad(-30))-100),0,"In the final product, there will be many more variations of these symbols"))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length),Unit(-unit_length+unit_length*np.sin(np.deg2rad(-30))),90,staff_1))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length+100),Unit(-unit_length+unit_length*np.sin(np.deg2rad(-30))+200),90,"The player may choose to stay in a region as long as they like to further explore the sound of that region"))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length),Unit(unit_length*np.sin(np.deg2rad(-30))),180,staff_1))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length-100),Unit(unit_length*np.sin(np.deg2rad(-30))+100),180,"In this example, the player decides to stay in the percussive region a little longer. In a moment you will see familiar text"))

    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length),Unit(unit_length*np.sin(np.deg2rad(-30))),90,staff_1))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length+100),Unit(unit_length*np.sin(np.deg2rad(-30))+200),90,"Now we move to the next region. Here we focus on sounds using Tambura"))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length+70),Unit(unit_length*np.sin(np.deg2rad(-30))+200),90,tamb_signpost, scale = 0.2))


    static_elements = np.append(static_elements,static_element(Unit(reg_2_x),Unit(-unit_length*np.sin(np.deg2rad(-30))),0,staff_1))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+200),Unit(-unit_length*np.sin(np.deg2rad(-30))-100),0,"We're approaching the end of the demo now!"))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length),Unit(-unit_length*np.sin(np.deg2rad(-30))),90,staff_1))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length+100),Unit(-unit_length*np.sin(np.deg2rad(-30))+100),90,"In each region, the effects chain used to process the sound of the guitar changes as well, helping to make the techniques have their own contextual meaning"))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length),Unit(unit_length-unit_length*np.sin(np.deg2rad(-30))),180,staff_1))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length-200),Unit(unit_length-unit_length*np.sin(np.deg2rad(-30))+100),180,"The full score will have many more regions, skills, and variations"))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x),Unit(unit_length-unit_length*np.sin(np.deg2rad(-30))),270,staff_1))
    static_elements = np.append(static_elements,static_element(Unit(reg_2_x-100),Unit(unit_length-unit_length*np.sin(np.deg2rad(-30))-200),270,"The current region determines what technique the performer is most likely to encounter"))

    static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length-80),Unit(-500),0,staff_30_junction_close))

    #static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length),Unit(unit_length*np.sin(np.deg2rad(-30))),30,staff_1))
    #static_elements = np.append(static_elements,static_element(Unit(reg_2_x+unit_length),Unit(-unit_length*np.sin(np.deg2rad(-30))),-30,staff_1))

    reg_3_x = reg_2_x+unit_length+unit_length*np.cos(np.deg2rad(30))
    static_elements = np.append(static_elements,static_element(Unit(reg_3_x+200),Unit(-100),0,"We've reached the end of the tech demo! Bye bye. Press any key to exit once the viewport stops moving."))
    #static_elements = np.append(static_elements,static_element(Unit(reg_3_x),Unit(0),0,staff_1))

    return static_elements

def go_forward(dur, dist, region, start_time, static_elements, HUD_elements):
    #This function removes the reference staff if present, then makes a new reference staff in the viewport and fills it with materials.
    #Once the materials are in place, the viewport translates.
    global staff, viewport_x_ini
    try:
        staff.remove()
    except:
        pass
    staff = make_reference_staff(viewport_x_ini)
    generate_staff_contents()
    def refresh_func_forward(time:float):
        global viewport_x_ini, viewport_y_ini, viewport_rot_ini
        global viewport_offset
        t = time-start_time
        neoscore.set_viewport_center_pos((viewport_x_ini + Unit(t*dist/dur) + viewport_offset,viewport_y_ini))
        if t >=dur:
            neoscore.set_viewport_center_pos((viewport_x_ini + Unit(dist) + viewport_offset,viewport_y_ini))
            viewport_x_ini = viewport_x_ini + Unit(dist)
            sequence(static_elements, HUD_elements)
        move_HUD(HUD_elements)
    neoscore.set_refresh_func(refresh_func_forward, framerate)

def go_rotate(rot_time, degrees, start_time, static_elements, HUD_elements):
    #This function rotates all the static elements after removing the reference staff and corresponding materials.
    global viewport_x_ini, viewport_y_ini, viewport_rot_ini
    global staff
    staff.remove()
    def refresh_func_rot(time:float):
        t = time-start_time
        move_HUD(HUD_elements)
        for i in range(static_elements.size):
            static_elements[i].obj_rotate(t,degrees,rot_time,viewport_x_ini,viewport_y_ini)
        if t >= rot_time:
            for i in range(static_elements.size):
                static_elements[i].confirm_obj_rotate(degrees,viewport_x_ini,viewport_y_ini)
            sequence(static_elements, HUD_elements)
    neoscore.set_refresh_func(refresh_func_rot, framerate)

def go_static():
    #This is called at the end of the demo to stop the motion of the viewport.
    try:
        staff.remove()
    except:
        pass
    def refresh_func_static(time:float):
        pass
    neoscore.set_refresh_func(refresh_func_static)

def send_particle():
    #This sends a message to SuperCollider. 
    global msg, macro_region
    msg.clearData()
    name = "string"
    if(macro_region == "A"):name = "scratchy_string"
    elif(macro_region == "B"):name = "plinky_wood"
    elif(macro_region == "C"):name = "cavernous_thunk"
    elif(macro_region == "Null"):name = "Null"
    else: print("what region is this!?")
    msg.append(name)
    try:
        client.send(msg)
    except:
        print("message failed to send to SuperCollider")

def update_effect(effect_name):
    global msg
    msg.clearData()
    msg.append(effect_name)
    try:
        client.send(msg)
    except:
        print("message failed to send to SuperCollider")

def sequence(static_elements, HUD_elements):
    #This very long block of code is only here for the demo. This is what automates navigation through the score.
    #This section will be greatly simplified when user input is used to navigate the score.
    global region, macro_region
    global skills, soundbank
    global scrape_HUD, perc_HUD, tamb_HUD, msg
    unit_length = 1000
    rate = 12 #12
    rot_rate = 4 #4
    start_time = time.time()
    #print("sequencing", region)
    if region == "loading":
        go_static()
        neoscore.set_key_event_handler(start_key)
    elif region == "A0":
        neoscore.set_key_event_handler(keyboard_off)
        update_effect("Region_1_effect")
        macro_region = "A"
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements) #format(duration(s), distance(px))
        region = "A1"
    elif region == "A1":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        soundbank = np.append(soundbank,tree_branch(skill = "star", image_path = star_1))
        region = "A2"
    elif region == "A2":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "A3"
    elif region == "A3":
        skills = np.append(skills,tree_branch(skill = "E_scrape_rank_1"))
        tree_branch.E_scrape_rank = 1
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "A4"
    elif region == "A4":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "A4_rot"
    elif region == "A4_rot":
        macro_region = "Null"
        go_rotate(rot_rate, 30, start_time, static_elements, HUD_elements)
        region = "A5_to_B1"
    elif region == "A5_to_B1":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "A5_to_B1_rot"
    elif region == "A5_to_B1_rot":
        macro_region = "B"
        go_rotate(rot_rate, 60, start_time, static_elements, HUD_elements)
        region = "B1"
    elif region == "B1":
        update_effect("Region_2_effect")
        skills = np.append(skills,tree_branch(skill = "perc_rank_1", image_path = perc_image[0], exp = 12, max_exp = 20, min_exp = 6))
        tree_branch.perc_rank = 1
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "B1_rot"
    elif region == "B1_rot":
        go_rotate(rot_rate, -90, start_time, static_elements, HUD_elements)
        region = "B2"
    elif region == "B2":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "B2_rot"
    elif region == "B2_rot":
        go_rotate(rot_rate, -90, start_time, static_elements, HUD_elements)
        region = "B3"
    elif region == "B3":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "B3_rot_cw"
    elif region == "B3_rot_cw":
        go_rotate(rot_rate, -90, start_time, static_elements, HUD_elements)
        region = "B4"
    elif region == "B4":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "B4_rot"
    elif region == "B4_rot":
        go_rotate(rot_rate, -90, start_time, static_elements, HUD_elements)
        region = "B1(2)"
    elif region == "B1(2)":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "B1_rot(2)"
    elif region == "B1_rot(2)":
        go_rotate(rot_rate, -90, start_time, static_elements, HUD_elements)
        region = "B2(2)"
    elif region == "B2(2)":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "B2_rot(2)"
    elif region == "B2_rot(2)":
        go_rotate(rot_rate, -90, start_time, static_elements, HUD_elements)
        region = "B3(2)"
    elif region == "B3(2)":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "B3_rot_straight"
    elif region == "B3_rot_straight":
        #go_rotate(rot_rate, 0)
        region = "B3_to_C2"
        sequence(static_elements, HUD_elements)
    elif region == "B3_to_C2":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "B3_to_C2_rot_straight"
    elif region == "B3_to_C2_rot_straight":
        update_effect("Region_3_effect")
        macro_region = "C"
        #go_rotate(rot_rate,0)
        region = "C2"
        sequence(static_elements, HUD_elements)
    elif region == "C2":
        skills = np.append(skills,tree_branch(skill = "tamb_rank_1", exp=20, max_exp=25, min_exp=15))
        tree_branch.tamb_rank = 1
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "C2_rot"
    elif region == "C2_rot":
        go_rotate(rot_rate, -90, start_time, static_elements, HUD_elements)
        region = "C3"
    elif region == "C3":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "C3_rot"
    elif region == "C3_rot":
        go_rotate(rot_rate, -90, start_time, static_elements, HUD_elements)
        region = "C4"
    elif region == "C4":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "C4_rot"
    elif region == "C4_rot":
        go_rotate(rot_rate, -90, start_time, static_elements, HUD_elements)
        region = "C1"
    elif region == "C1":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "C1_rot_ccw"
    elif region == "C1_rot_ccw":
        go_rotate(rot_rate, 30, start_time, static_elements, HUD_elements)
        region = "C1_to_D1"
    elif region == "C1_to_D1":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "C1_to_D1_rot"
    elif region == "C1_to_D1_rot":
        go_rotate(rot_rate, -30, start_time, static_elements, HUD_elements)
        region = "D1"
    elif region == "D1":
        go_forward(rate, unit_length, region, start_time, static_elements, HUD_elements)
        region = "D2"
    else: go_static(), neoscore.set_key_event_handler(exit_key)
    return region

def make_HUD():
    #This generates all elements in the Heads-Up Display and sticks them in an array.
    x,y = neoscore.get_viewport_center_pos()
    HUD_elements = np.array([])
    reticle_path = Path((Unit(-10),Unit(110)),None, Brush.no_brush(), pen = Pen("000000",Unit(4), PenPattern.DOT))
    reticle_path.line_to(Unit(0),Unit(-140))
    reticle_path.line_to(Unit(20),Unit(-140))
    reticle_path.line_to(Unit(20),Unit(0))
    reticle_path.line_to(Unit(0),Unit(0))
    HUD_elements = np.append(HUD_elements, reticle_path)
    reticle = Text((Unit(0),Unit(0)), None, " ")
    HUD_elements = np.append(HUD_elements, reticle)
    staff_for_clef = Staff((Unit(20),Unit(0)), None, Unit(500), line_spacing=Unit(20), pen = (Pen(pattern = PenPattern.INVISIBLE)))
    HUD_elements = np.append(HUD_elements, staff_for_clef)
    clef = Clef(ZERO, staff_for_clef, 'treble')
    HUD_elements = np.append(HUD_elements, clef)
    time_text = Text((x-Unit(200), Unit(-150)), None, "0.00")
    HUD_elements = np.append(HUD_elements, time_text)
    scrape_level_text = Text((x-Unit(-230),Unit(-150)),None, "Scrape: ")
    HUD_elements = np.append(HUD_elements, scrape_level_text)
    perc_level_text = Text((x-Unit(-180),Unit(-150)),None, "Perc: ")
    HUD_elements = np.append(HUD_elements, perc_level_text)
    tamb_level_text = Text((x-Unit(-120),Unit(-150)),None, "Tamb: ")
    HUD_elements = np.append(HUD_elements, tamb_level_text)
    return HUD_elements

def move_HUD(HUD_elements):
    #This ensures the HUD is glued to the viewport.
    x,y = neoscore.get_viewport_center_pos()
    HUD_elements[0].x = x - Unit(200) #reticle
    HUD_elements[1].x = x             #blank reference
    HUD_elements[2].x = x - Unit(200) #clef
    #Element 3 is the staff
    HUD_elements[4].x = x - Unit(300) #time
    total_time = float(time.time())-program_start_time
    HUD_elements[4].text = ("{:#.2f}"+" seconds").format(total_time)
    HUD_elements[5].x = x - Unit(-230) #scrape level
    HUD_elements[5].text = ("Scrape: " + str(tree_branch.E_scrape_rank))
    HUD_elements[6].x = x - Unit(-180) #perc level
    HUD_elements[6].text = ("Perc: " + str(tree_branch.perc_rank))
    HUD_elements[7].x = x - Unit(-120) #perc level
    HUD_elements[7].text = ("Tamb: " + str(tree_branch.tamb_rank))

def make_reference_staff(viewport_x_ini):
    #This is the staff upon which performance materials are placed. 
    #This is invisible, but it is lined up exactly with the map-staff so the pitches are accurate.
    staff = Staff((viewport_x_ini-Unit(20),Unit(0)), None, Unit(500), line_spacing=Unit(20), pen = (Pen(pattern = PenPattern.INVISIBLE)))
    invisible_clef = Clef(Unit(-1000), staff, 'treble', pen = (Pen(pattern = PenPattern.INVISIBLE)))
    return staff

def generate_staff_contents():
    #This is the function which primarily uses the class tree_branch and generates staff materials.
    global cells, skills, soundbank, staff
    cells = np.array([])
    weights = np.array([])
    number_of_cells = 4
    skill_indicies = np.arange(skills.size)
    for i in range(skills.size):
        weights = np.append(weights,skills[i].exp)
    #print("weights: ", weights)
    if weights.size > 0:
        weighted_list = random.choices(skill_indicies, weights, k=number_of_cells)
        for i in range(number_of_cells):
            skills[weighted_list[i]].exp_gain
            cells = np.append(cells,skills[weighted_list[i]].generate_cell(5+i*10))
    if soundbank.size > 0: 
        cells = np.append(cells,soundbank[0].generate_cell(15))
        send_particle()
    #cells = np.append(cells,soundbank[0].generate_cell(5+10*random.randint(1,4)))
    
def exit_key(event):
    #This is used only at the very end of the demo.
    neoscore.shutdown()

def start_key(event):
    #This is used to start the demo.
    global region, static_elements, HUD_elements, program_start_time
    region = "A0"
    program_start_time = int(time.time())
    sequence(static_elements, HUD_elements)

def keyboard_off(event):
    pass


def main():
    global region
    global viewport_x_ini, viewport_y_ini, viewport_rot_ini
    global viewport_offset
    global staff
    global skills, soundbank, cells
    global static_elements, HUD_elements
    viewport_x_ini = Unit(0)
    viewport_y_ini = Unit(0)
    viewport_rot_ini = 0
    viewport_offset = Unit(200)
    region = "loading"
    neoscore.setup()

    skills = np.array([])
    soundbank = np.array([])
    cells = np.array([])

    static_elements = np.array([])
    static_elements = make_map(static_elements)

    HUD_elements = make_HUD()
    staff = make_reference_staff(viewport_x_ini)

    make_render_area()

    sequence(static_elements, HUD_elements)
    neoscore.set_viewport_center_pos((Unit(0)+viewport_offset,Unit(0)))
    neoscore.set_viewport_scale(2)
    neoscore.show(display_page_geometry=False, auto_viewport_interaction_enabled=False, min_window_size=(1280,720), max_window_size=(1280,720))

if __name__ == '__main__':
    #Connection to Supercollider initiation
    client = pyOSC3.OSCClient()
    client.connect( ( '127.0.0.1', 57120 ) )
    msg = pyOSC3.OSCMessage()
    msg.setAddress("/print")
    #Load images
    perc_image = np.array([])
    for filename in os.listdir("Assets/perc_images"):
        perc_image = np.append(perc_image, "Assets/perc_images/"+filename)
    staff_angle_30 = pathlib.Path("Assets")/"staff_angle_30.png"
    staff_angle_60 = pathlib.Path("Assets")/"staff_angle_60.svg"
    staff_30_junction = pathlib.Path("Assets")/"staff_30_junction.png"
    staff_30_junction_close = pathlib.Path("Assets")/"staff_30_junction_close.png"
    test_image_1 = pathlib.Path("Assets")/"test_image_1.png"
    test_image_2 = pathlib.Path("Assets")/"test_image_2.png"
    test_image_3 = pathlib.Path("Assets")/"test_image_3.png"
    test_image_4 = pathlib.Path("Assets")/"test_image_4.png"
    test_image_5 = pathlib.Path("Assets")/"test_image_5.png"
    perc_signpost = pathlib.Path("Assets")/"percussionville.png"
    tamb_signpost = pathlib.Path("Assets")/"tambura_land.png"
    staff_1 = pathlib.Path("Assets")/"staff_1000px.png"
    guit_cell_1 = pathlib.Path("Assets")/"squiggle_1.png"
    star_1 = pathlib.Path("Assets")/"star_1.png"
    disk_1 = pathlib.Path("Assets")/"disk.png"
    sul_6 = pathlib.Path("Assets")/"Sul_6.png"
    #Get program start time
    main()
