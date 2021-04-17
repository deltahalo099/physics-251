# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:38:38 2020

@author: Omar Abdelaal
"""
import math

#function definition to caclulate volume and surface area
#prints in proper format

def sphereinfo(r):
    surface_area = 4*math.pi*(r**2)
    volume = (4/3)*math.pi*(r**3)
    
    print('for radius r = {}'.format(r))
    print("surface area {} m^2".format(surface_area))
    print("volume {} m^3".format(volume))

#function calls
sphereinfo(1.0)
sphereinfo(10.0)