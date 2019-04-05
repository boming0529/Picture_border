from PIL import Image, ExifTags
import numpy as np
import os


# step0 open flag & camera picture and get current workspace path
cwspath = os.getcwd()

src_path = cwspath + '\\src\\'
camera = Image.open(src_path + "Camera.jpg").convert('RGB')
camera = camera.resize((int(camera.width*0.3), int(camera.height*0.3)), Image.ANTIALIAS)
camera = np.array(camera)
camera[:, :, 2][camera[:, :, 2] >= 30] -= 30

flag = Image.open(src_path + "Denmark.jpg").convert('RGB')
flag = flag.resize((int(flag.width*0.085), int(flag.height*0.085)), Image.ANTIALIAS)
flag = np.array(flag)

logo = Image.open(src_path + "logo.jpg").convert('RGB')
logo = np.array(logo)

path = cwspath + '\\origin\\'
Picture = os.listdir(path)
k = -1
while k < len(Picture) - 1:
    k += 1
    Photo = Image.open(path + Picture[k])

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

    width = Photo.width
    height = Photo.height
    print(width, height, Photo.size)

    Photo = Photo.resize(
        (int(Photo.width*0.25), int(Photo.height*0.25)), Image.ANTIALIAS)
    Photo_arr = np.array(Photo)
    if not R:
        new_bg = 255 * np.ones([630+70, 944, 3], dtype=np.uint8)
        new_bg[:, :, 2][new_bg[:, :, 2] >= 30] -= 30
        new_bg[0:630, 0:944] = Photo_arr
        new_bg[640: 692-1, 21: 90-1] = flag
        new_bg[635: 699-1, 110:361-1] = logo
        new_bg[634: 696-1, 859: 940-1] = camera
    else:
        new_bg = 255 * np.ones([944+70, 630, 3], dtype=np.uint8)
        new_bg[:, :, 2][new_bg[:, :, 2] >= 30] -= 30
        new_bg[0:944, 0:630] = Photo_arr
        new_bg[954:1006-1, 21:90-1] = flag
        new_bg[949:1013-1, 110:361-1] = logo
        new_bg[950:1012-1, 534:615-1] = camera
    im = Image.fromarray(new_bg)
    im.save(cwspath + '\\bs_pic\\' + Picture[k], quality=95)

# step1 open origin image.
# img = Image.open("simple.jpg")

# step2 create background image.
# new_bg = 255 * np.ones([1477+70, 1108, 3], dtype=np.uint8)
# new_bg[:,:,2] =- 30

# setp3 convert origin and new image to np.array formatter
# img_arr = np.array(img)
#
# setp4 do your process
# new_bg[0:1477, 0:1108] = img_arr
# setp5 convert to image frommter and save
# im = Image.fromarray(new_bg)
# im.save("test.jpeg", quality=90)

# step2 you can using new image
# new_img = Image.new('RGB', (1108, 1477+70))

# step3 you sould change np array formmter
# new_img_arr = np.array(new_img)
