import random
import glob
import os

dir_res_gen = os.path.join('.','assets','gen')

def initialize_generated_sources():
    if not os.path.exists(dir_res_gen):
        os.makedirs(dir_res_gen)
    for f in glob.glob(f"{dir_res_gen}/*"):
        os.remove(f)

def get_name(seed,ext,length=10):
    random.seed(str(seed))
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    chars = "".join(random.sample(valid_chars,length))
    return f"{dir_res_gen}{chars}.{ext}"

def get_asset(name):
    return os.path.join('.','assets',name)