import os
import random
import shutil

off_zones = []

def migrate(new_dir):
    current_dir = os.getcwd()
    shutil.move(current_dir, new_dir)

def find_possible_paths(starting_point):
    legal_paths = []
    os.chdir(starting_point)
    
    while True:
        new_path = scout_dir()
        if new_path:  
            legal_paths.append(new_path)
            print(f"Found directory: {new_path}")
        else:
            break  

def scout_dir() -> str:
    directories = [x for x in os.listdir() if os.path.isdir(x) and "." not in x]
    
    if directories:
        chosen_dir = random.choice(directories)
        return os.path.join(os.getcwd(), chosen_dir)
    return None  

def init():

    root = None
    for _ in range(10):
        if "Downloads" in os.listdir():
            root = os.getcwd()
            break
        os.chdir("..")  
    
    if root:
        find_possible_paths(root)

if __name__ == "__main__":
    init()
