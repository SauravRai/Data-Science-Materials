
from PIL import Image
import os

import numpy as np
import cv2

directory = 'a'
count = 2704
basewidth = 400

for filename in os.listdir(directory):	
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        #print(filename)
        input_image = Image.open(f)  
        wper = (basewidth/float(input_image.size[0]))
        hsize = int((float(input_image.size[1]) * float(wper)))  
        input_image = input_image.resize((basewidth, hsize), Image.ANTIALIAS)
        
        newFilename = str(count) + "_" + filename
        #print(newFilename)
        #show image
        input_image.show()
        input_image.save(newFilename)


print("DONE")



