# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:24:13 2020

@author: Omar Abdelaal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# symbols and colors for plot
smbl=['1','.','x','1','2','3','4','_','^','>','<','|']
clr=['r','b','g','m','orange','coral','limegreen',
     'purple', 'brown', 'tan', 'gold', 'grey']

def fx(theta):
    y = np.sin(theta)
    return y

#initial conditons
theta = 30 * np.pi/180
w = 0
t0 = 0
tf = 15
dt = .1

t = np.arange(t0, tf, dt)
print(t)
    
#forward euler algorithm
for k in range(t.size):
    theta[k+1] = theta[k] + dt*fx(t[k])
    w[k+1] = w[k] - dt*theta[k]

#Euler-Cromer algorithm
for k in range(t.size):
    w[k+1] = w[k] - dt*theta[k]
    theta[k+1] = theta[k] + dt*w[k+1]