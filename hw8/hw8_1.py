# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:23:32 2020

@author: Omar Abdelaal
"""
import numpy as np
import matplotlib.pyplot as plt

# symbols and colors for plot
smbl=['1','.','x','1','2','3','4','_','^','>','<','|']
clr=['r','b','g','m','orange','coral','limegreen',
     'purple', 'brown', 'tan', 'gold', 'grey']

def F1(y, t):
    dydt = t*np.exp(3*t) - 2*y
    return dydt

def F2(y, t):
    dydt = 1 + (t-y)**2
    return dydt

def F3(y, t):
    dydt = 1 + y/t
    return dydt

def F4(y, t):
    dydt = np.cos(2*t) + np.sin(3*t)
    return dydt


# problem a---------------------------
y0 = 0  #initial condition
t0 = 0  #inital time
tf = 1  #final time

dt = np.array([.5, .1, .05, .01])
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
        y[k+1] = y[k] + dt[i]*F1(y[k], t[k])
    
    plt.plot(t,y,smbl[i],color=clr[i], label='$\Delta t$={}'.format(dt[i]))

plt.title('problem a')
plt.grid()
plt.legend()

# problem b---------------------------
y0 = 1
t0 = 2
tf = 3

dt = np.array([.5, .1, .05, .01])
ndt = dt.size

plt.figure(2)
#loop for dt
for i in range(ndt):
    nt = int((tf-t0)/dt[i]) + 1
    t = np.linspace(t0, tf, num=nt)
    y = np.zeros(nt)
    y[0] = y0
    
    #forward euler algorithm
    for k in range(nt - 1):
        y[k+1] = y[k] + dt[i]*F2(y[k], t[k])
    
    plt.plot(t,y,smbl[i],color=clr[i], label='$\Delta t$={}'.format(dt[i]))

plt.title('problem b')
plt.grid()
plt.legend()

# problem c---------------------------
y0 = 1
t0 = 1
tf = 2

dt = np.array([.25, .1, .05, .01])
ndt = dt.size

plt.figure(3)
#loop for dt
for i in range(ndt):
    nt = int((tf-t0)/dt[i]) + 1
    t = np.linspace(t0, tf, num=nt)
    y = np.zeros(nt)
    y[0] = y0
    
    #forward euler algorithm
    for k in range(nt - 1):
        y[k+1] = y[k] + dt[i]*F3(y[k], t[k])
    
    plt.plot(t,y,smbl[i],color=clr[i], label='$\Delta t$={}'.format(dt[i]))

plt.title('problem c')
plt.grid()
plt.legend()

# problem d---------------------------
y0 = 0
t0 = 0
tf = 2*np.pi

dt = np.array([.25, .1, .05, .01])
ndt = dt.size

plt.figure(4)
#loop for dt
for i in range(ndt):
    nt = int((tf-t0)/dt[i]) + 1
    t = np.linspace(t0, tf, num=nt)
    y = np.zeros(nt)
    y[0] = y0
    
    #forward euler algorithm
    for k in range(nt - 1):
        y[k+1] = y[k] + dt[i]*F4(y[k], t[k])
    
    plt.plot(t,y,smbl[i],color=clr[i], label='$\Delta t$={}'.format(dt[i]))

plt.title('problem d')
plt.grid()
plt.legend()