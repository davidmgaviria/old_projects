# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image

counter = 2
path = 'C:/Users/David Gaviria/Documents/Paradox Interactive/Hearts of Iron IV/mod/fractured_earth/gfx/flags/small/'
file = 'C:/Users/David Gaviria/Documents/Paradox Interactive/Hearts of Iron IV/mod/fractured_earth/gfx/flags/small/001.tga'
extension = '.tga'

while counter<764:
    myImage = Image.open(file)
        
    if counter < 10:
        name = path+'00'+str(counter)+'.tga'
        myImage.save(name)
        
    elif counter > 9 and counter <100:
        name = path+'0'+str(counter)+'.tga'
        myImage.save(name)
        
    else:
        name = path+str(counter)+'.tga'
        myImage.save(name)
        
    counter += 1
    

print('Done')
