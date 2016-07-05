#!/usr/bin/env python
from images2gif import writeGif
from PIL import Image
import os
#from IPython.display import Image

file_names = ['doge2.jpg', 'doge3.jpg', 'doge4.jpg']

images = [Image.open(fn) for fn in file_names]

size = (600,350)
for im in images:
    im.thumbnail(size, Image.ANTIALIAS)

filename = "doge.gif"
writeGif(filename, images, duration=0.5, subRectangles=False)

