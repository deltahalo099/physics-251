# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:27:43 2020

@author: Omar Abdelaal
"""
import numpy as np
import matplotlib.pyplot as plt

# symbols and colors for plot
smbl=['1','.','x','1','2','3','4','_','^','>','<','|']
clr=['r','b','g','m','orange','coral','limegreen',
     'purple', 'brown', 'tan', 'gold', 'grey']

def F1(t):
    dydt = -9.8*t
    return dydt

# problem a---------------------------
y0 = 1000    #initial condition
t0 = 0       #inital time
tf = 10      #final time

dt = np.array([.01, .1, 1.0])
ndt = dt.size

plt.figure(1)
#loop for dt
for i in range(ndt):
    nt = int((tf-t0)/dt[i]) + 1
    t = np.linspace(t0, tf, num=nt)
    y = np.zeros(nt)
    y[0] = y0
    
    #forward euler algorithm
    for k in range(nt - 1):
        y[k+1] = y[k] + dt[i]*F1(t[k])
    
    plt.plot(t,y,smbl[i],color=clr[i], label='$\Delta t$={}'.format(dt[i]))

plt.title('problem a')
plt.grid()
plt.legend()