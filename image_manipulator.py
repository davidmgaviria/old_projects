# -*- coding: utf-8 -*-
"""
Image Manipulator
Created by David M. Gaviria at the University of Gereogia Tech
"""
#%%
#Global variables and modules
from scipy import misc
from shapely.geometry import Point, Polygon
from ctypes import *
import matplotlib.pyplot as plt
import tkinter as tk
import os

global line_drawn, moving_points, erasing_points, allPoints, xDPI, yDPI
global xValues, yValues, list_spot, plotting, image, savedWidths, savedHeights, savedArea, saveIndex

savedWidths = dict()
savedHeights = dict()
savedAreas = dict()
line_drawn = False
plotting = False
moving_points = False
erasing_points = False
allPoints = dict()
xValues = []
yValues = []
list_spot = -1
saveIndex = 0
#%%
def plotPoint(x,y):
    global allPoints, i
    new_point = plt.scatter(x, y, c='c', s=15)
    plt.draw()
    xValues.append(x)
    yValues.append(y)
    allPoints[x, y] = new_point
#%%
def findPoint(ix,iy):
    global list_spot
    x_in_range = False
    y_in_range = False
    Searching = True
    list_spot = -1
    
    for x, y in zip(xValues, yValues):
        if Searching == True:
            list_spot += 1
            if ix > x:
                if x+2 > ix:
                    x_in_range = True
            else:
                if x-2 < ix:
                    x_in_range = True  
            if iy > y:
                if y+2 > iy:
                    y_in_range = True    
            else:
                if y-2 < iy:
                    y_in_range = True
        
            if x_in_range == True and y_in_range == True:
                global specPoint, rid, mid
                specPoint = allPoints[x,y]
                del allPoints[x,y]
                Searching = False
        
                if moving_points == True:
                    rid = plt.connect('button_release_event', on_release)
                    mid = mid = plt.connect('motion_notify_event', mouse_move)
                elif erasing_points == True:
                    specPoint.set_offsets((None,None))
                    plt.draw()
                    xValues.remove(x)
                    yValues.remove(y)
                else:
                    pass
                
            else:
                 x_in_range = False
                 y_in_range = False
        else:
            break 
#%%
def drawLine():
    global line, line_drawn, xValues, yValues
    if line_drawn == False:
        totalX, totalY = xValues, yValues
        totalX.append(xValues[0])
        totalY.append(yValues[0])
        xValues = xValues[:-1]
        yValues = yValues[:-1]
        line = plt.plot(totalX, totalY, 'y-', linewidth = 2)
        plt.draw()
        line_drawn = True
    else:
        print('Line is already drawn')
#%%
def deleteLine():
    global line, line_drawn
   
    plt.setp(line, xData=0, yData=0, linewidth = 0)
    plt.draw()
    line_drawn = False
#%%
def imageProcessing():
    global xValues, yValues, image, permPoints
    print('Processing... please wait')
    
    coords = []
    for x,y in zip(xValues, yValues):
        coords.append((x,y))
    
    poly = Polygon(coords)
    
    count, pixelNum = 0, 0
    for point in image:
        count +=1
        
    x, y = 0, 0
    while y<(count+1):
        for i in range(count):
            x +=1
            #print(x,y)
            p = Point(x,y)
            if p.within(poly)==True:
                pixelNum +=1
        x = 0
        y+=1
    
    Calculate(pixelNum)
#%%
def Calculate(pixelNum):
    global xDPI, yDPI
    
    pixel_width = 2.54/xDPI        #centimeters
    pixel_height = 2.54/yDPI       #centimeters
    pixel_area = pixel_width*pixel_height 
    
    area = pixel_area*pixelNum
    width = (max(xValues) - min(xValues))*pixel_width
    height = (max(yValues) - min(yValues))*pixel_height
    area = round(area, 2)
    width = round(width,2)
    height = round(height,2)
    
    print('Width: {} cm    Height: {} cm    Area: {} cm{}'.format(width, height, area, chr(0x00B2)))
    newPlot(width, height, area)
#%%
def newPlot(width, height, area):
    global allPoints, xValues, yValues, line_drawn, line, saveIndex

    saveIndex+=1
    savedWidths[saveIndex] = width
    savedHeights[saveIndex] = height
    savedAreas[saveIndex] = area
    
    plt.setp(line, color='white', linestyle = '--')
    plt.draw()
    line = ''
    line_drawn = False
#    for x,y in allPoints:
#        point = allPoints[x,y]
#        point.set_offsets(color = 'white')
#        plt.draw()
    allPoints = dict()
    xValues = []
    yValues = []
#%%
def Ratio():
    global savedWidths, savedHeights, savedAreas, saveIndex
    
    print('The width ratio is ', end='')
    for i in range(saveIndex):
        print('{}cm' .format(savedWidths[i+1]), end='/')
        
    print('\nThe height ratio is ', end='')
    for i in range(saveIndex):
        print('{}cm' .format(savedHeights[i+1]), end='/')
       
    print('\nThe area ratio is ', end='')
    for i in range(saveIndex):
        print('{}cm{}' .format(savedAreas[i+1],chr(0x00B2)), end='/')
        
#%%
def on_release(event):
    global mid, rid, Searching, specPoint
    ix, iy = event.xdata, event.ydata
    allPoints[ix, iy] = specPoint
    plt.disconnect(mid)
    plt.disconnect(rid)
#%%
def mouse_move(event):
    global xValues, yValues, list_spot, line_drawn
    ix, iy = event.xdata, event.ydata
    specPoint.set_offsets((ix, iy))
    xValues[list_spot] = ix
    yValues[list_spot] = iy
    if line_drawn == True:
        deleteLine()
        drawLine()
    plt.pause(0.001)
#%%
def on_click(event):
    global moving_points, erasing_points
    ix, iy = event.xdata, event.ydata
    
    if moving_points == True or erasing_points == True:
        findPoint(ix, iy)
    else: 
        if line_drawn == False:
            plotPoint(ix, iy)
        else:
            print('Line is already drawn, delete line to add points')
#%%
def plotCommands(event):
    global plotting, line_drawn, moving_points, erasing_points, xValues, cid, saveIndex
    
    if event.key == 'd':
        if plotting == False:
            print('Point plotting enabled')
            cid = plt.connect('button_press_event', on_click)
            plotting = True
        else:
            print('Point plotting disabled')
            plt.disconnect(cid)
            plotting = False
            erasing_points = False
            moving_points = False
    
    elif event.key == 'e':
        if plotting == True:
            if line_drawn == False:
                if erasing_points == False:
                    erasing_points = True
                    moving_points = False
                    plotting = False
                    print('Point erasing enabled')
                else:
                    erasing_points = False
                    plotting = True
                    print('Point erasing disabled')
            else:
                print('Delete line first')
        else:
            print('Place a point first')
            
    elif event.key == 'm':
        if plotting == True:
            if moving_points == False:
                moving_points = True
                erasing_points = False
                plotting = False
                print('Point moving enabled')
            else:
                moving_points = False
                plotting = True
                print('Point moving disabled')
        else:
            print('Place a point first')
        
    elif event.key == 'j':
        if line_drawn == False:
            if len(xValues)>1:
                drawLine()
            else:
                print('Insufficent points to draw line')
        else:
            deleteLine()
            moving_points = False
            erasing_points = False
                
    elif event.key == 'c':
        if line_drawn == True:
            moving_points = False
            erasing_points = False
            plotting = False
            print('All point functions diabled')
            imageProcessing()
        else:
            print('No area exists')
            
    elif event.key == 'r':
        if saveIndex>1:
            Ratio()
        else:
            print('At least 2 selections are required to compute a ratio')
    else:
        print('Invalid key, enter "d", "e", "j", "m", "c", or "r."')
#%%
def Run():
    global image
    choosing = True
    while choosing:
        try:
            #pic_name = ' '     #set a default pic for debugging
            pic_name = input('Open file: ')
            if pic_name.startswith('C:/') or pic_name.startswith('C:\r'):
                image = misc.imread(pic_name)
                choosing = False
            else:
                pic_path = 'C:/Users/dgaviria6/.spyder-py3/my_saved_images/'
                image = misc.imread(os.path.join(pic_path, pic_name))
                choosing = False
        except:
            print('No such file or directory: {}{}\n' .format(pic_path,pic_name))
            print('Make sure you typed the file name correctly, including the file extension \n'
                  'A default path is set, to change it, type in the full path and file name, including the file extension\n')
            
    plt.connect('key_press_event', plotCommands)
    print('Press "d" to enable or disable point plotting.\n'
          'Press "e" to enable or disable point erasing.\n'
          'Press "m" to enable or disable point moving.\n'
          'Press "j" to draw or delete the line connecting the points.\n'
          'Press "c" to obtain the measurements of the enclosed area.')
    plt.axis('off')
    plt.imshow(image)
    plt.show()
#%%
def screenProperty():
    global xDPI, yDPI
    
    root = tk.Tk()
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    #print(screen_width,screen_height)
    
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    dc = windll.user32.GetDC(0)
    xDPI = windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
    yDPI = windll.gdi32.GetDeviceCaps(dc, LOGPIXELSY)
    windll.user32.ReleaseDC(0, dc)
    #print("Horizontal DPI is", hDPI )
    #print("Vertical DPI is", vDPI)
#%%
if __name__=='__main__':
    print('Image Manipulator\n'
    'Created by David M. Gaviria at the University of Gereogia Tech\n')
    screenProperty()
    Run()