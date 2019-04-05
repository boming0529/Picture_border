from PIL import Image

im = Image.open("src\simple.jpg")

print (im.format, im.size, im.mode)