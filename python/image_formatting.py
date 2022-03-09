import os, glob, numpy as np, requests, random
from PIL import Image, ImageDraw, ImageFilter
from io import BytesIO

def image_format_circular(img):
    npImage = np.array(img.convert('RGBA'))
    h,w = img.size

    alpha = Image.new('L',img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.ellipse((0,0,h,w),fill=255)

    img.putalpha(alpha.filter(ImageFilter.GaussianBlur(4)))

    return img

def image_read(path):
    return Image.open(path)

def image_src(url):
    return Image.open(BytesIO(requests.get(url).content))

def image_format(img,make_circular=False,width=-1,height=-1):
    image = img
    if make_circular:
        image = image_format_circular(image)
    
    if width != -1:
        if height != -1:
            image = image.resize((width,height))
        else:
            image = image.resize((width,image.size[1]))
    elif height != -1:
        image = image.resize((image.size[0],height))
    
    return image