import os
import random
import shutil
import json
main_dir = os.getcwd()

def migrate(new_dir):
    # print(new_dir)
    update_history(new_dir)
    shutil.move(main_dir, new_dir)

def update_history(new_dir):
    print("s")
    history_file_path = os.path.join(main_dir, "history.json")
    with open(history_file_path, "r") as file:
        cool = json.load(file)
 
    cool["path"] = new_dir
    cool["history"]["prev path"] = main_dir  
    print(cool)
    with open(history_file_path, "w") as file:
        json.dump(cool, file, indent=4)

def find_possible_paths(starting_point):
    legal_paths = []
    os.chdir(starting_point)
    
    for i in range(5):
        new_path = scout_dir()
        if new_path:  
            legal_paths.append(new_path)
        else:
            break
    if legal_paths:
        migrate(random.choice(legal_paths))  

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
