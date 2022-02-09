# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 22:17:11 2019

@author: David Gaviria
"""

#%%
import os
from pathlib import Path

directory = "C:/Users/david/Desktop/Wipe-Folder"

folder = [directory]


for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        open(Path(directory)/filename, 'w').close
    else:
        folder.append(directory+"/"+filename)
        
        
for item in folder:
    for filename in os.listdir(item):
        if filename.endswith(".txt"):
            open(Path(item)/filename, 'w').close
            
print('Done')
          

    
