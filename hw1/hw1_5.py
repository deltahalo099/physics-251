# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:59:02 2020

@author: Omar Abdelaal
"""

import math

#constants
G = 6.67e-11
M = 5.97e24
R = 6371000


def altitude(t):
    h = (((G*M*t**2)/(4*math.pi**2))**1/3)-R
    return h

#because the formula is in seconds first we need to convert all times to seconds    
#a. t = 24 hrs
t = 24*60*60
print('the altitude for a 24 hour period is: ' + str(altitude(t)))

#b. t = 90 minutes
t = 90*60    
print('the altitude for a 90 minute period is: ' + str(altitude(t)))   

#c. t = 45 minutes
t = 45*60
print('the altitude for a 45 minute period is: ' + str(altitude(t)))   

"""
from these three calculations we can conclude that
the altitude of an orbiting satellite is directly proportional to the period
"""

t_day = 24*60*60
t_sidereal = 23.93*60*60

#compare
print('the difference in altitude between a 24hr day and a sidereal day is: ' + str(altitude(t_day) - altitude(t_sidereal)))
