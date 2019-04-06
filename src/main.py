# -*- coding: utf-8 -*-
from PIL import Image, ExifTags
import numpy as np
import os


class Pictures(object):

    def __init__(self, img):
        self._img = img

    def imresize(self, scope):
        scope = scope if scope > 0 else 1
        _width = int(self._img.width * scope)
        _height = int(self._img.height * scope)
        return self._img.resize((_width, _height), Image.ANTIALIAS)


# Read flag, camera and logo picture and get current workspace path
cwspath = os.getcwd()
src_path = cwspath + '\\src\\'

camera = Image.open(src_path + "Camera.jpg").convert('RGB')
camera = Pictures(camera).imresize(0.3)
camera = np.array(camera)
camera[:, :, 2][camera[:, :, 2] >= 30] -= 30

flag = Image.open(src_path + "China.png").convert('RGB')
flag = Pictures(flag).imresize(0.09)

logo = Image.open(src_path + "china_logo.jpg").convert('RGB')
logo = Pictures(logo).imresize(0.95)

path = cwspath + '\\origin\\'
Picture = os.listdir(path)
k = -1
while k < len(Picture) - 1:
    k += 1
    if Picture[k] == '.gitkeep':
        continue
    Photo = Image.open(path + Picture[k])
    # image processing
    R = False
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(Photo._getexif().items())
    # if exif[orientation] == 3:
    #     Photo = Photo.rotate(180, expand=True)
    if exif[orientation] == 6:
        Photo = Photo.rotate(270, expand=True)
        R = True
    elif exif[orientation] == 8:
        Photo = Photo.rotate(90, expand=True)
        R = True
    print(Picture[k])
    
    Photo = Pictures(Photo).imresize(0.25)
    new_bg = 255 * \
        np.ones([Photo.height + 70, Photo.width, 3], dtype=np.uint8)
    new_bg[:, :, 2][new_bg[:, :, 2] >= 30] -= 30
    im = Image.fromarray(new_bg)

    if not R:
        im.paste(Photo, (0, 0))
        im.paste(flag, (21, 640))
        im.paste(logo, (110, 635))
        im.paste(Image.fromarray(camera), (859, 634))
    else:
        im.paste(Photo, (0, 0))
        im.paste(flag, (21, 954))
        im.paste(logo, (110, 949))
        im.paste(Image.fromarray(camera), (534, 950))
    # save
    im.save(cwspath + '\\bs_pic\\' + Picture[k], quality=95)
