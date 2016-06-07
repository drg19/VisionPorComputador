from Tkinter import *
import sys, os#, Image, ImageTk
from PIL import Image
from numpy import array, zeros
from matplotlib.pyplot import imshow, show, subplot, gray, title, axis


imagen = Image.open('2.jpg')#= sys.argv[1]
width, height = imagen.size
level_min = 100
level_max = 200

for w in range(width):
    for h in range(height):
        r, g, b = imagen.getpixel((w, h))
        gray = (r+g+b)/3
        if gray < level_min:
            imagen.putpixel((w, h), (0, 0, 0))
        elif gray > level_max:
            imagen.putpixel((w, h), (255, 255, 255))
        else:
            imagen.putpixel((w, h), (gray, gray, gray))

subplot(1, 1, 1)
imshow(imagen)
axis('off')
title('Umbrales')

show()