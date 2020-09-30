# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:24:07 2018

@author: drodr
"""

import numpy as np
import matplotlib.pyplot as mplot
from PIL import Image
from os import listdir
from os.path import isfile, join
#delete images 1, 4, 7, 9, 13, 18, 131, 133, 138, 143

userinput = int(input("Enter a threshold value between 0 and 255: "))

while userinput < 0 or userinput > 255:
    userinput = int(input("Invalid Input. Enter a threshold value between 0 and 255: "))

images = [f for f in listdir("einsteinatanderson") if isfile(join("einsteinatanderson", f))]

img = []
for index in range(0, len(images)):
    image = Image.open("einsteinatanderson/" + images[index])
    img.append(np.float64(image))

average_image = img[0]
for index in range(1, len(img)):
    average_image += img[index]
average_image /= len(img)

abs_image = abs(img[0]-img[-1])
for index in range(1, len(img)):
    abs_image += np.square(abs(img[index] - img[0]))
abs_image /= len(img)

std_dev_image = np.sqrt(abs_image)

#loops over each row of the image
for row in range(0, len(std_dev_image)):
 #loops over each column of the image
     for col in range(0, len(std_dev_image[row])):
 #if the pixel at position [row][col] has any
 #color elements greater than user input
         if (std_dev_image[row][col] > [userinput, userinput, userinput]).any():
 #if so, then we set that pixel's color to Red
             average_image[row][col]=[255, 0, 0]

average_image = np.clip(average_image, 0, 255)
abs_image = np.clip(abs_image, 0, 255)
average_image = np.uint8(average_image)
abs_image = np.uint8(abs_image)
mplot.imshow(average_image)
mplot.show()
