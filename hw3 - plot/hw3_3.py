# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:09:26 2020

@author: Ziron
"""

import matplotlib.pyplot as plt
import numpy as np

#needed constants and variables
v0 = 40.0
g = 9.8

v0x = v0*np.cos(45)
v0y = v0*np.sin(45)

x0 = 0
y0 = 0
t = np.linspace(0, 7, 100)

#function for x position
def x(t):
  x = x0 + v0x*t
  return x

#function for y position
def y(t):
  y = y0 + v0y*t - (1/2)*g*t**2
  return y

#function of x velocity
def vx(t):
  vx = v0x + 0*t
  return vx

#function of y velocity
def vy(t):
  vy = v0y - g*t
  return vy

"""
#plot of x and y with respect to t
xtime, = plt.plot(x(t), label = 'x vs t')
ytime, = plt.plot(y(t), label = 'y vs t')

plt.legend(handles = [xtime, ytime])
plt.title('position vs. time')
plt.ylabel('position (m)')
plt.xlabel('time')
plt.grid()


#plot of vx and vy with respect to t
vxtime, = plt.plot(vx(t), label = 'vx vs t')
vytime, = plt.plot(vy(t), label = 'vy vs t')

plt.legend(handles = [vxtime, vytime])
plt.title('velocity vs time')
plt.ylabel('velocity')
plt.xlabel('time')
plt.grid()

"""
#plot of ball trajectory
plt.plot(x(t), y(t))
plt.title('trajectory of ball')
plt.ylabel('y position')
plt.xlabel('x position')
plt.grid()
