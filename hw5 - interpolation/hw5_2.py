# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:34:23 2020

@author: Omar Abdelaal
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('fc_thist_00520.txt', skip_header = 2)

t = data[:,0]
s1 = data[:,7]
nt = t.size



def interpolation(xi, x1, y1, x2, y2):
  yi = y1 + (xi - x1)*(y2 - y1)/(x2 - x1)
  return yi
    
    
# part 1
# tint = [1, 2, 3, ..., 400]
dt = 10.0
t0 = 1.0
tn = 400.0
nint = int((tn-t0)/dt) + 1

tint = np.linspace(t0, tn, num=nint)
sint = np.zeros(nint)

for j in range(nint):
    for i in range(nt):
        if t[i] > tint[j]:
            x1 = t[i-1]
            x2 = t[i]
            y1 = s1[i-1]
            y2 = s1[i]
            xi = tint[j]
            sint[j] = interpolation(xi, x1, y1, x2, y2)
            break
        
plt.figure()
plt.plot(t, s1, label='raw data')
plt.xlabel('time')
plt.ylabel('concentration')
plt.grid()
plt.legend()

plt.figure()
plt.plot(t, s1, label='raw data')
plt.plot(tint, sint, '.r', label = 'interpolation dt = 10')
plt.xlabel('time')
plt.ylabel('concentration')
plt.grid()
plt.legend()
