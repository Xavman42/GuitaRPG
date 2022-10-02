class Plevel:
    """Class containing all the player level information for each skill
    
    """
    
    test_dict = {'reg 1' : 0, 'reg 2' : 1, 'reg 3' : 2, 'reg 4' : 3}
    
    
    def __init__(
        self,
        num_of_skills: int = 4,
        initial_skill_level: int = 1,
        maximum_skill_level: int = 5,
    ):
        self.num_of_skills = num_of_skills
        self.initial_skill_level = initial_skill_level
        self.maximum_skill_level = maximum_skill_level
        self.current_skill_level = [initial_skill_level] * num_of_skills
        self.skill_xp_min = [1] * num_of_skills
        self.skill_xp_max = [5] * num_of_skills
        self.skill_xp_rate = [1] * num_of_skills
        self.current_xp = self.skill_xp_min * num_of_skills
    
#    @property
#    def num_of_skills(self) -> int:
#        """The total number of skills(regions) in the piece"""
#        return self._num_of_skills
    
#    @num_of_skills.setter
#    def num_of_skills(self, value: int):
#        self._num_of_skills = value
        
    def xp_up(
        self,
        skill: int
    ):
        if(self.current_xp[skill] >= self.skill_xp_max[skill]):
            self.current_xp[skill] = self.skill_xp_min[skill]
            if(self.current_skill_level[skill] < self.maximum_skill_level):
                self.current_skill_level[skill] = self.current_skill_level[skill] + 1
        self.current_xp[skill] = self.current_xp[skill] + self.skill_xp_rate[skill]
        return self.current_skill_level