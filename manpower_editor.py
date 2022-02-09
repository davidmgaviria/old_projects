# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:15:50 2019

@author: David Gaviria
"""
#%%
import os
from pathlib import Path

directory = "C:/Users/David Gaviria/Documents/Paradox Interactive/Hearts of Iron IV/mod/fractured_earth/history/states"
count = 0

for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        count+=1
        fhand = open(Path(directory)/filename)
        for line in fhand:
            if line.startswith("	manpower"):
                index = line.find('=')
                manpower = int(line[index+1:].replace(" ", ""))
                new_manpower = int(manpower/5)
                print(filename+": "+new_manpower)
    else:
        continue
    
print("Done")
