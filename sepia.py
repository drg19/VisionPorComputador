from Tkinter import *
import sys, os#, Image, ImageTk
from PIL import Image
from numpy import array, zeros
from matplotlib.pyplot import imshow, show, subplot, gray, title, axis


imagen = Image.open('2.jpg')#= sys.argv[1]
width, height = imagen.size
sepia_intensity = 50

for w in range(width):
    for h in range(height):
        r, g, b = imagen.getpixel((w, h))
        gray = (r+g+b)/3
        r = gray + (sepia_intensity * 2)
        g = gray + sepia_intensity
        b = gray - sepia_intensity

        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b < 0:
            b = 0
        imagen.putpixel((w, h), (r, g, b))

subplot(1, 1, 1)
imshow(imagen)
axis('off')
title('Sepia')

show()
