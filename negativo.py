from Tkinter import *
import sys, os#, Image, ImageTk
from PIL import Image
from numpy import array, zeros
from matplotlib.pyplot import imshow, show, subplot, gray, title, axis


imagen = Image.open('2.jpg')#= sys.argv[1]
width, height = imagen.size

for w in range(width):
    for h in range(height):
        r, g, b = imagen.getpixel((w, h))
        gray = (r+g+b)/3
        imagen.putpixel((w, h), (255-r, 255-g, 255-b))

subplot(1, 1, 1)
imshow(imagen)
axis('off')
title('Negativo')

show()