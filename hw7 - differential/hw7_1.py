# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:50:06 2020

@author: Omar Abdelaal
"""
import numpy as np
import matplotlib.pyplot as plt

#df/dx of fx = cos x + sin x
# x = [0, 2pi]
domain = np.linspace(0, 2*np.pi, 100)

#our function
def f1(x):
    y = np.cos(x) + np.sin(x)
    return y

#analytical derivative of function
def dfdx(x):
    dfdx = -np.sin(x) + np.cos(x)
    return dfdx


#forward difference method
def forward_aprx(myf, x, dx):
    dfdx_f = (myf(x + dx) - myf(x)) / dx
    return dfdx_f
    
#backward difference method
def backward_aprx(myf, x, dx):
    dfdx_b = (myf(x) - myf(x - dx)) / dx
    return dfdx_b

#central difference method
def central_aprx(myf, x, dx):
    dfdx_c = (myf(x + dx) - myf(x - dx)) / (2*dx)
    return dfdx_c


#GETTING OUR APPROXIMATIONS
dx = domain[2] - domain[1]

#storing our approximations in an array
forward = np.zeros(100)
backward = np.zeros(100)
central = np.zeros(100)

#for loop for generating the approximations
for i in range(domain.size - 1):
    forward[i] = forward_aprx(f1, domain[i], dx)
    backward[i] = backward_aprx(f1, domain[i], dx)
    central[i] = central_aprx(f1, domain[i], dx)
    
   
#plotting
plt.plot(f1(domain), '.', label='function')
plt.plot(dfdx(domain), '.', label="analytical derivative")
plt.plot(forward, '.', label = 'forward difference')
plt.plot(backward, '.', label = "backward difference")
plt.plot(central, '.', label = "central difference")
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel('df/dx')