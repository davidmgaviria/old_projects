# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:58:26 2018

@author: David Gaviria
"""

#%%
import folium
map = folium.Map(
    location=[45.372, -121.6972],
    zoom_start=12,
    tiles='Mapbox Bright'
)

map.save('map.html')
