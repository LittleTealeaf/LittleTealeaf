import random
import glob
import os

dir_res_gen = os.path.join('.','assets','gen')

def clean_gens():
    for f in glob.glob(f"{dir_res_gen}/*"):
        os.remove(f)

def get_name(seed,ext,length=10):
    random.seed(str(seed))
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    chars = "".join(random.sample(valid_chars,length))
    return f"{dir_res_gen}{chars}.{ext}"
