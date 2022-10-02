import os
import numpy as np

#script_dir = os.path.dirname(__file__)
#print(script_dir)
#print(os.listdir("C:\\Users\\xavie\\GuitaRPG\\GuitaRPG\\Assets\\perc_images"))
#print(os.path.join(script_dir, os.listdir("./Assets/perc_images")))


#script_dir = os.path.dirname(__file__)
#file_path = os.path.join(script_dir, './Assets/perc_images')
#print(file_path)

from pathlib import Path

working_directory = Path(os.getcwd())
path = working_directory / "Assets" / "perc_images"
print(path)

for filename in path.listdir:
        perc_image = np.append(perc_image, "Assets/perc_images/"+filename)