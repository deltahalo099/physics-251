# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:56:47 2020

@author: Ziron
"""

#newtonian motion under constant acceleration
def newton(t):
  y0 = 100.00           #initial position
  v0 = 0.0              #initial velocity
  g = 9.8               #acceleration
  y = y0 + v0*t - (1/2)*g*t**2
  
  return y
  

#A CLOCK!!!!
tn = 0              #start time
dt = 0.5            #increment

while (tn<100):
  tn = tn + dt
  print('time: {}'.format(tn))
  print(newton(tn))



