from PIL import Image, ImageFilter

im = Image.opne('demo.PNG')
# show figure
im.show()   
# figure sharpen
im_sharp = im.filter(ImageFilter.SHARPEN)
# split RGBA channel (band)
if im_sharp.mode == 'RGBA':
    r,g,b,a = im_sharp.split()
elif im_sharp.mode == 'RGB':
    r,g,b = im_sharp.split()

# show be inserted EXIF tags in figure
exif_data = im._getexif()
exif_data