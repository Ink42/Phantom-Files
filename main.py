import os
import shutil



def migrate(new_dir):
    shutil.move(os.getcwd(),new_dir)

