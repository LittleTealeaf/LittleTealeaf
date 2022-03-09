import random
import glob
import json
import os

dir_res_gen = os.path.join('.','assets','gen')

def initialize_assets():
    if not os.path.exists(dir_res_gen):
        os.makedirs(dir_res_gen)
    for f in glob.glob(f"{dir_res_gen}/*"):
        os.remove(f)

def generate_asset_name(seed,ext,length=10):
    random.seed(str(seed))
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    chars = "".join(random.sample(valid_chars,length))
    return f"{chars}.{ext}"

def get_asset_path(name):
    if type(name) == str:
        return os.path.join('.','assets',name)
    else:
        return os.path.join('.','assets',*name)

def generate_asset_path(seed, ext, length = 10):
    return get_asset_path(['gen',generate_asset_name(seed,ext,length)])

def load_json(path):
    file = open(path)
    data = json.load(file)
    file.close()
    return data

