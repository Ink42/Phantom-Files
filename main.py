import os
import random
import shutil


off_zones =[]

def migrate(new_dir):
    shutil.move(os.getcwd(),new_dir)

def find_possible_paths(starting_point):
    legal_paths =[]
    os.chdir(starting_point)
    off_zones = os.listdir()
    print(off_zones)
    for i in os.listdir():
        if  "." not in i:
            legal_paths.append(i)
      
            
    if legal_paths: 
        chosen_path = os.path.join(os.getcwd(), random.choice(legal_paths))        
        print(os.chdir(chosen_path))
        print(os.listdir())
        print("level 1")
        chosen_path = os.path.join(os.getcwd(), random.choice(os.listdir()))        
        print(os.chdir(chosen_path))
        print(os.listdir())
        print("level 2")


    # print(len(ee))


def init():
    root = None
    for _ in range(10):
        if "Downloads" in os.listdir():
            root = os.getcwd()
            break
        os.chdir("..") 
        
    if root:
        find_possible_paths(root)
    

  

if __name__=="__main__":
   init()
