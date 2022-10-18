#import Image from PIL

from PIL import Image
import os

directory = 'PolyNodules'
angle = 90 #45 #90 #135
count = 2704
for filename in os.listdir(directory):	
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        #print(filename)
        input_image = Image.open(f)  
        #print(input_image)     
        input_image = input_image.rotate(angle)
        newFilename = str(count) + "_" + filename
        #print(newFilename)
        input_image.save(newFilename)   
print("DONE")


