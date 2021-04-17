# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:49:09 2020

@author: Omar Abdelaal
"""

import numpy as np
import matplotlib.pyplot as plt

# symbols and colors for plot
smbl=['1','.','x','1','2','3','4','_','^','>','<','|']
clr=['r','b','g','m','orange','coral','limegreen',
     'purple', 'brown', 'tan', 'gold', 'grey']


# problem a---------------------------
v0 = 0.0
y0 = 1000    #initial condition
t0 = 0       #inital time
tf = 10      #final time
g = 9.8

dt = np.array([.01, .1, 1.0])
ndt = dt.size

plt.figure(1)
#loop for dt
for i in range(ndt):
    nt = int((tf-t0)/dt[i]) + 1
    t = np.linspace(t0, tf, num=nt)
    y = np.zeros(nt)
    y[0] = y0
    v = np.zeros(nt)
    v[0] = v0
    
    #forward euler algorithm
    for k in range(nt - 1):
        y[k+1] = y[k] + dt[i]*(-g*t[k])
        v[k+1] = -g*t[k] + dt[i]*(-g)
    
    plt.plot(t,y,smbl[i],color=clr[i], label='$\Delta t$={}'.format(dt[i]))
    plt.plot(t,v,smbl[i],color=clr[i], label='$\Delta t$={}'.format(dt[i]))
plt.title('problem a')
plt.grid()
plt.legend()