# -*- coding: utf-8 -*-
def convertTemp():
    temp =  input('Farenheit Temperature: ')
    try:
        fahr = float(temp)
        cel = (fahr - 32) * 5/9
        print('Celsius Temperature: {}'.format(cel))
        print('Done')
    except:
        print('Please enter a number')
        convertTemp()

convertTemp()