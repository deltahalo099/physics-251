# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:50:06 2020

@author: Omar Abdelaal
"""
import numpy as np
import matplotlib.pyplot as plt

#df/dx of fx = cos x + sin x
# x = [0, 2pi]
domain = np.linspace(-5, 5, 200)

#our function
def f1(x):
    y = np.exp(-x**2)
    return y

#analytical derivative of function
def dfdx(x):
    dfdx = -2*x*np.exp(-x**2)
    return dfdx

#analytical second derivative
def dfdx2(x):
    dfdx2 = (4*x**2 - 2)*np.exp(-x**2)
    return dfdx2

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

#second order central difference method
def my2ndcentral(myf, x, dx):
    dfdx2 = (myf(x + dx) - 2*myf(x) + myf(x - dx)) / dx**2
    return dfdx2

#GETTING OUR APPROXIMATIONS
dx = domain[2] - domain[1]

#storing our approximations in an array
forward = np.zeros(200)
backward = np.zeros(200)
central = np.zeros(200)
secondorder = np.zeros(200)

#for loop for generating the approximations
for i in range(domain.size - 1):
    forward[i] = forward_aprx(f1, domain[i], dx)
    backward[i] = backward_aprx(f1, domain[i], dx)
    central[i] = central_aprx(f1, domain[i], dx)
    secondorder[i] = my2ndcentral(f1, domain[i], dx)
    
   
#plotting
plt.plot(f1(domain), '.', label='function')
plt.plot(dfdx(domain), '.', label="analytical derivative")
plt.plot(dfdx2(domain), '.', label="analytical 2nd derivative")
plt.plot(forward, '.', label = 'forward difference')
plt.plot(backward, '.', label = "backward difference")
plt.plot(central, '.', label = "central difference")
plt.plot(secondorder, '.', label = "second order central")
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel('df/dx')
