from Tkinter import *
import sys, os#, Image, ImageTk
from PIL import Image
from numpy import array, zeros
from matplotlib.pyplot import imshow, show, subplot, gray, title, axis


imagen = Image.open('2.jpg')#= sys.argv[1]
width, height = imagen.size
image_copy = imagen

for sx in range(2):
    for w in range(width):
        for h in range(height):
            if w > 0 and w < width-1 and h > 0 and h < height-1:
                r1, g1, b1 = image_copy.getpixel((w, h))
                r2, g2, b2 = image_copy.getpixel((w, h-1))
                r3, g3, b3 = image_copy.getpixel((w-1, h))
                r4, g4, b4 = image_copy.getpixel((w, h+1))
                r5, g5, b5 = image_copy.getpixel((w+1, h))
                r, g, b = ((r1+r2+r3+r4+r5)/5,
                           (g1+g2+g3+g4+g5)/5,
                           (b1+b2+b3+b4+b5)/5)
                imagen.putpixel((w, h), (r, g, b))

subplot(1, 1, 1)
imshow(imagen)
axis('off')
title('Promedios')

show()