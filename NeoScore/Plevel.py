from Cells import *


def make_cell_dict():
    # Dictionary format: 'key': [probability, function, area multiplier, region multiplier]
    default_probability = 0
    area_modifier = 1
    region_modifier = 1
    cell_dict = {'scrape_rank_1': [default_probability, scrape_rank_1, area_modifier, region_modifier, "scrape"],
                 'scrape_rank_2': [default_probability, scrape_rank_2, area_modifier, region_modifier, "scrape"],
                 'scrape_rank_3': [default_probability, scrape_rank_3, area_modifier, region_modifier, "scrape"],
                 'scrape_rank_4': [default_probability, scrape_rank_4, area_modifier, region_modifier, "scrape"],
                 'bartok_rank_1': [default_probability, bartok_rank_1, area_modifier, region_modifier, "bartok"],
                 'bartok_rank_2': [default_probability, bartok_rank_2, area_modifier, region_modifier, "bartok"],
                 'bartok_rank_3': [default_probability, bartok_rank_3, area_modifier, region_modifier, "bartok"],
                 'bartok_rank_4': [default_probability, bartok_rank_4, area_modifier, region_modifier, "bartok"],
                 'tambura_rank_1': [default_probability, tambura_rank_1, area_modifier, region_modifier, "tambura"],
                 'tambura_rank_2': [default_probability, tambura_rank_2, area_modifier, region_modifier, "tambura"],
                 'tambura_rank_3': [default_probability, tambura_rank_3, area_modifier, region_modifier, "tambura"],
                 'tambura_rank_4': [default_probability, tambura_rank_4, area_modifier, region_modifier, "tambura"],
                 'perc_rank_1': [default_probability, perc_rank_1, area_modifier, region_modifier, "perc"],
                 'perc_rank_2': [default_probability, perc_rank_2, area_modifier, region_modifier, "perc"],
                 'perc_rank_3': [default_probability, perc_rank_3, area_modifier, region_modifier, "perc"],
                 'perc_rank_4': [default_probability, perc_rank_4, area_modifier, region_modifier, "perc"],
                 'triad_rank_1': [default_probability, triad_rank_1, area_modifier, region_modifier, "triad"],
                 'triad_rank_2': [default_probability, triad_rank_2, area_modifier, region_modifier, "triad"],
                 'triad_rank_3': [default_probability, triad_rank_3, area_modifier, region_modifier, "triad"],
                 'triad_rank_4': [default_probability, triad_rank_4, area_modifier, region_modifier, "triad"],
                 'melody_rank_1': [default_probability, melody_rank_1, area_modifier, region_modifier, "melody"],
                 'melody_rank_2': [default_probability, melody_rank_2, area_modifier, region_modifier, "melody"],
                 'melody_rank_3': [default_probability, melody_rank_3, area_modifier, region_modifier, "melody"],
                 'melody_rank_4': [default_probability, melody_rank_4, area_modifier, region_modifier, "melody"],
                 'harmonic_rank_1': [default_probability, harmonic_rank_1, area_modifier, region_modifier, "harmonic"],
                 'harmonic_rank_2': [default_probability, harmonic_rank_2, area_modifier, region_modifier, "harmonic"],
                 'harmonic_rank_3': [default_probability, harmonic_rank_3, area_modifier, region_modifier, "harmonic"],
                 'harmonic_rank_4': [default_probability, harmonic_rank_4, area_modifier, region_modifier, "harmonic"],
                 'rake_rank_1': [default_probability, rake_rank_1, area_modifier, region_modifier, "rake"],
                 'rake_rank_2': [default_probability, rake_rank_2, area_modifier, region_modifier, "rake"],
                 'rake_rank_3': [default_probability, rake_rank_3, area_modifier, region_modifier, "rake"],
                 'rake_rank_4': [default_probability, rake_rank_4, area_modifier, region_modifier, "rake"],
                 'tremolo_rank_1': [default_probability, tremolo_rank_1, area_modifier, region_modifier, "tremolo"],
                 'tremolo_rank_2': [default_probability, tremolo_rank_2, area_modifier, region_modifier, "tremolo"],
                 'tremolo_rank_3': [default_probability, tremolo_rank_3, area_modifier, region_modifier, "tremolo"],
                 'tremolo_rank_4': [default_probability, tremolo_rank_4, area_modifier, region_modifier, "tremolo"],
                 'adv_harm_rank_1': [default_probability, adv_harm_rank_1, area_modifier, region_modifier, "adv_harm"],
                 'adv_harm_rank_2': [default_probability, adv_harm_rank_2, area_modifier, region_modifier, "adv_harm"],
                 'adv_harm_rank_3': [default_probability, adv_harm_rank_3, area_modifier, region_modifier, "adv_harm"],
                 'adv_harm_rank_4': [default_probability, adv_harm_rank_4, area_modifier, region_modifier, "adv_harm"]}
    return cell_dict


def make_xp_dict():
    default_xp = 0
    default_level = 0
    xp_dict = {'scrape': [1, default_xp],
               'bartok': [default_level, default_xp],
               'tambura': [default_level, default_xp],
               'perc': [default_level, default_xp],
               'melody': [default_level, default_xp],
               'harmonic': [default_level, default_xp],
               'rake': [default_level, default_xp],
               'tremolo': [default_level, default_xp],
               'adv_harm': [default_level, default_xp],
               'rasg': [default_level, default_xp],
               'triad': [default_level, default_xp]}
    return xp_dict


def increase_xp(xp_dict, key):
    xp_dict[key][1] += 1
    if xp_dict[key][1] >= 5 and xp_dict[key][0] < 4:
        xp_dict[key][0] += 1
        xp_dict[key][1] = 0
    return xp_dict, xp_dict[key][0]


def initialize_skill(xp_dict, cell_dict, key):
    try:
        if xp_dict[key][0] == 0:
            xp_dict[key][0] = 1
            set_skill_probability(cell_dict, key, 1)
    except KeyError:
        pass
    return xp_dict, cell_dict


def apply_area_modifier(cell_dict, area):
    default_mod = 1
    area_mod_value = 10
    for i, j in cell_dict.items():
        j[2] = default_mod
    if area == 1:
        cell_dict['scrape_rank_1'][2] = area_mod_value
        cell_dict['scrape_rank_2'][2] = area_mod_value
        cell_dict['scrape_rank_3'][2] = area_mod_value
        cell_dict['scrape_rank_4'][2] = area_mod_value
        cell_dict['bartok_rank_1'][2] = area_mod_value
        cell_dict['bartok_rank_2'][2] = area_mod_value
        cell_dict['bartok_rank_3'][2] = area_mod_value
        cell_dict['bartok_rank_4'][2] = area_mod_value
        cell_dict['tambura_rank_1'][2] = area_mod_value
        cell_dict['tambura_rank_2'][2] = area_mod_value
        cell_dict['tambura_rank_3'][2] = area_mod_value
        cell_dict['tambura_rank_4'][2] = area_mod_value
        cell_dict['perc_rank_1'][2] = area_mod_value
        cell_dict['perc_rank_2'][2] = area_mod_value
        cell_dict['perc_rank_3'][2] = area_mod_value
        cell_dict['perc_rank_4'][2] = area_mod_value

    elif area == 2:
        cell_dict['triad_rank_1'][2] = area_mod_value
        cell_dict['triad_rank_2'][2] = area_mod_value
        cell_dict['triad_rank_3'][2] = area_mod_value
        cell_dict['triad_rank_4'][2] = area_mod_value
        cell_dict['melody_rank_1'][2] = area_mod_value
        cell_dict['melody_rank_2'][2] = area_mod_value
        cell_dict['melody_rank_3'][2] = area_mod_value
        cell_dict['melody_rank_4'][2] = area_mod_value
        cell_dict['harmonic_rank_1'][2] = area_mod_value
        cell_dict['harmonic_rank_2'][2] = area_mod_value
        cell_dict['harmonic_rank_3'][2] = area_mod_value
        cell_dict['harmonic_rank_4'][2] = area_mod_value
        cell_dict['rake_rank_1'][2] = area_mod_value
        cell_dict['rake_rank_2'][2] = area_mod_value
        cell_dict['rake_rank_3'][2] = area_mod_value
        cell_dict['rake_rank_4'][2] = area_mod_value

    elif area == 3:
        cell_dict['tremolo_rank_1'][2] = area_mod_value
        cell_dict['tremolo_rank_2'][2] = area_mod_value
        cell_dict['tremolo_rank_3'][2] = area_mod_value
        cell_dict['tremolo_rank_4'][2] = area_mod_value
        cell_dict['adv_harm_rank_1'][2] = area_mod_value
        cell_dict['adv_harm_rank_2'][2] = area_mod_value
        cell_dict['adv_harm_rank_3'][2] = area_mod_value
        cell_dict['adv_harm_rank_4'][2] = area_mod_value
    return cell_dict


def apply_region_modifier(cell_dict, region, region_mod_value=10):
    default_mod = 1
    for i, j in cell_dict.items():
        j[3] = default_mod
    if region == "scrape":
        cell_dict['scrape_rank_1'][3] = region_mod_value
        cell_dict['scrape_rank_2'][3] = region_mod_value
        cell_dict['scrape_rank_3'][3] = region_mod_value
        cell_dict['scrape_rank_4'][3] = region_mod_value
    elif region == "bartok":
        cell_dict['bartok_rank_1'][3] = region_mod_value
        cell_dict['bartok_rank_2'][3] = region_mod_value
        cell_dict['bartok_rank_3'][3] = region_mod_value
        cell_dict['bartok_rank_4'][3] = region_mod_value
    elif region == "tambura":
        cell_dict['tambura_rank_1'][3] = region_mod_value
        cell_dict['tambura_rank_2'][3] = region_mod_value
        cell_dict['tambura_rank_3'][3] = region_mod_value
        cell_dict['tambura_rank_4'][3] = region_mod_value
    elif region == "perc":
        cell_dict['perc_rank_1'][3] = region_mod_value
        cell_dict['perc_rank_2'][3] = region_mod_value
        cell_dict['perc_rank_3'][3] = region_mod_value
        cell_dict['perc_rank_4'][3] = region_mod_value
    elif region == "triad":
        cell_dict['triad_rank_1'][3] = region_mod_value
        cell_dict['triad_rank_2'][3] = region_mod_value
        cell_dict['triad_rank_3'][3] = region_mod_value
        cell_dict['triad_rank_4'][3] = region_mod_value
    elif region == "melody":
        cell_dict['melody_rank_1'][3] = region_mod_value
        cell_dict['melody_rank_2'][3] = region_mod_value
        cell_dict['melody_rank_3'][3] = region_mod_value
        cell_dict['melody_rank_4'][3] = region_mod_value
    elif region == "harmonic":
        cell_dict['harmonic_rank_1'][3] = region_mod_value
        cell_dict['harmonic_rank_2'][3] = region_mod_value
        cell_dict['harmonic_rank_3'][3] = region_mod_value
        cell_dict['harmonic_rank_4'][3] = region_mod_value
    elif region == "rake":
        cell_dict['rake_rank_1'][3] = region_mod_value
        cell_dict['rake_rank_2'][3] = region_mod_value
        cell_dict['rake_rank_3'][3] = region_mod_value
        cell_dict['rake_rank_4'][3] = region_mod_value
    elif region == "tremolo":
        cell_dict['tremolo_rank_1'][3] = region_mod_value
        cell_dict['tremolo_rank_2'][3] = region_mod_value
        cell_dict['tremolo_rank_3'][3] = region_mod_value
        cell_dict['tremolo_rank_4'][3] = region_mod_value
    elif region == "adv_harm":
        cell_dict['adv_harm_rank_1'][3] = region_mod_value
        cell_dict['adv_harm_rank_2'][3] = region_mod_value
        cell_dict['adv_harm_rank_3'][3] = region_mod_value
        cell_dict['adv_harm_rank_4'][3] = region_mod_value
    else:
        for i, j in cell_dict.items():
            j[3] = default_mod
    return cell_dict


def set_skill_probability(cell_dict, skill, level):
    if level == 0:
        l1 = 0
        l2 = 0
        l3 = 0
        l4 = 0
    elif level == 1:
        l1 = 1
        l2 = 0
        l3 = 0
        l4 = 0
    elif level == 2:
        l1 = 1
        l2 = 2
        l3 = 0
        l4 = 0
    elif level == 3:
        l1 = 1
        l2 = 2
        l3 = 3
        l4 = 0
    elif level == 4:
        l1 = 1
        l2 = 1
        l3 = 1
        l4 = 2
    if skill == "scrape":
        cell_dict['scrape_rank_1'][0] = l1
        cell_dict['scrape_rank_2'][0] = l2
        cell_dict['scrape_rank_3'][0] = l3
        cell_dict['scrape_rank_4'][0] = l4
    elif skill == "bartok":
        cell_dict['bartok_rank_1'][0] = l1
        cell_dict['bartok_rank_2'][0] = l2
        cell_dict['bartok_rank_3'][0] = l3
        cell_dict['bartok_rank_4'][0] = l4
    elif skill == "tambura":
        cell_dict['tambura_rank_1'][0] = l1
        cell_dict['tambura_rank_2'][0] = l2
        cell_dict['tambura_rank_3'][0] = l3
        cell_dict['tambura_rank_4'][0] = l4
    elif skill == "perc":
        cell_dict['perc_rank_1'][0] = l1
        cell_dict['perc_rank_2'][0] = l2
        cell_dict['perc_rank_3'][0] = l3
        cell_dict['perc_rank_4'][0] = l4
    elif skill == "triad":
        cell_dict['triad_rank_1'][0] = l1
        cell_dict['triad_rank_2'][0] = l2
        cell_dict['triad_rank_3'][0] = l3
        cell_dict['triad_rank_4'][0] = l4
    elif skill == "melody":
        cell_dict['melody_rank_1'][0] = l1
        cell_dict['melody_rank_2'][0] = l2
        cell_dict['melody_rank_3'][0] = l3
        cell_dict['melody_rank_4'][0] = l4
    elif skill == "harmonic":
        cell_dict['harmonic_rank_1'][0] = l1
        cell_dict['harmonic_rank_2'][0] = l2
        cell_dict['harmonic_rank_3'][0] = l3
        cell_dict['harmonic_rank_4'][0] = l4
    elif skill == "rake":
        cell_dict['rake_rank_1'][0] = l1
        cell_dict['rake_rank_2'][0] = l2
        cell_dict['rake_rank_3'][0] = l3
        cell_dict['rake_rank_4'][0] = l4
    elif skill == "tremolo":
        cell_dict['tremolo_rank_1'][0] = l1
        cell_dict['tremolo_rank_2'][0] = l2
        cell_dict['tremolo_rank_3'][0] = l3
        cell_dict['tremolo_rank_4'][0] = l4
    elif skill == "adv_harm":
        cell_dict['adv_harm_rank_1'][0] = l1
        cell_dict['adv_harm_rank_2'][0] = l2
        cell_dict['adv_harm_rank_3'][0] = l3
        cell_dict['adv_harm_rank_4'][0] = l4
    return cell_dict


def get_cell_func(cell_dict):
    function_list = []
    key_list = []
    for key, value in cell_dict.items():
        key_list.append(key)
        function_list.append(value[1])
    probability_list = []
    for key, value in cell_dict.items():
        probability_list.append(value[0])
    area_modifier_list = []
    for key, value in cell_dict.items():
        area_modifier_list.append(value[2])
    region_modifier_list = []
    for key, value in cell_dict.items():
        region_modifier_list.append(value[3])
    mod_list = []
    for i in range(len(probability_list)):
        mod_list.append(probability_list[i]*area_modifier_list[i]*region_modifier_list[i])
    index_list = list(range(0, len(function_list)))
    random_number = random.choices(index_list, mod_list)[0]
    my_choice = function_list[random_number]
    for key, value in cell_dict.items():
        if value[1] == my_choice:
            my_region = value[4]
    return my_choice, my_region


if __name__ == '__main__':
    my_cell_dict = make_cell_dict()
    my_cell_dict = apply_area_modifier(my_cell_dict, 1)
    my_cell_dict = set_skill_probability(my_cell_dict, "scrape", 4)
    my_cell_dict = apply_region_modifier(my_cell_dict, "scrape", 100)
    my_xp_dict = make_xp_dict()
    for i in range(12):
        my_xp_dict, lvl = increase_xp(my_xp_dict, "scrape")

    get_cell_func(my_cell_dict)
    # for i in range(20):
    #    print(my_cell_dict.items())
    #  for key, value in my_cell_dict.items():
    #      print(value)
