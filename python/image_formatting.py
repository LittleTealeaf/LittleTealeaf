from email.mime import image
import os
import glob
import numpy as np
import requests
import random

from PIL import Image, ImageDraw, ImageFilter
from io import BytesIO

img_res = './assets/imgs/'
name_length = 10

if not os.path.exists(img_res):
    os.makedirs(img_res)

for f in glob.glob(f"{img_res}/*"):
    os.remove(f)

def circular(img):
    npImage = np.array(img.convert('RGBA'))
    h,w = img.size

    alpha = Image.new('L',img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.ellipse((0,0,h,w),fill=255)

    img.putalpha(alpha.filter(ImageFilter.GaussianBlur(4)))

    return img
    
def generate_source_name(seed):
    random.seed(seed)
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    return "".join(random.sample(chars,10)) + ".png"

def image_format_src(src,make_circular=False,width=-1,height=-1):
    response = requests.get(src)
    image = Image.open(BytesIO(response.content)).convert('RGBA')

    if make_circular:
        image = circular(image)
    
    if width != -1 and height != -1:
        image = image.resize((width,height))

    saveName = img_res + " " + generate_source_name(src + str(make_circular) + str(width) + str(height))

    image.convert('RGBA').save(saveName)
    return saveName