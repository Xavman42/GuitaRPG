import enum
from Plevel import Plevel

level = Plevel()
print(level.current_skill_level)


test_dict = {'all' : 1, 'food' : 2, 'good' : 3, 'have' : 4}


res = list(test_dict.keys()).index('good')
print(str(res))

print(level.xp_up(2))
print(level.xp_up(3))
















































