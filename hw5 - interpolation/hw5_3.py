# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:23:09 2020

@author: Omar Abdelaal
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

data = np.genfromtxt('data_2d_grid_T.txt', skip_header = 13)

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]
t = data[:, 3]

#DATA 3D PLOT
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_trisurf(x, y, z, cmap=cm.terrain,linewidth=0, antialiased=False)
plt.show()


#BILINEAR INTERPOLATION
dq = 41     #gap between y1 and y2
tx = 39*39  #number of rectangles

#to store our interpolated values
xint = np.zeros(tx)
yint = np.zeros(tx)
zint = np.zeros(tx)

#for loop for the formula
for i in range(tx):
    xhlf = 0.5* (x[i+1] + x[i])
    yhlf = 0.5* (y[i+dq] + y[i])
    
    a =      z[i]*(x[i+1] - xhlf)*(y[dq+i] - yhlf)
    b =     z[dq+i]*(x[i+1] - xhlf)*(yhlf - y[i])
    c =      z[i+1]*(xhlf - x[i])*(y[dq+i] - yhlf)
    d =     z[dq+i+1]*(xhlf - x[i])*(yhlf - y[i])
    
    ztemp = (a+b+c+d)/((x[i+1]-x[i])*((y[dq+i])-y[i]))
    
    xint[i] = xhlf
    yint[i] = yhlf
    zint[i] = ztemp
    
#plotting the interpolation

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_trisurf(xint, yint, zint, cmap=cm.terrain,linewidth=0, antialiased=False)
plt.show()

