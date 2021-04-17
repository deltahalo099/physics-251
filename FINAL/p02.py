# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:40:32 2020

@author: Omar Abdelaal
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#function
def fx(x):
    y = np.exp(-.1*x) * (1 + np.cos(np.pi/4 * x)**2)**.5
    return y

#plot
domain = np.arange(-10, 10, .1)  
plt.plot(fx(domain))
plt.grid()

#simpsons method
def my_simpson(myf, a, b, n):
    dx = (b-a)/n
    
    xi = a
    A = 0.0
    for i in range(n):
        xip1 = xi + dx
        ximid = (xi + xip1)/2.0
        A = A + myf(xi) + 4.0*myf(ximid) + myf(xip1)
        xi = xip1
    
    A = A * dx/6.0   
    
    return A

#integrating!
print(my_simpson(fx, -10, 10, 5))
print(my_simpson(fx, -10, 10, 10))
print(my_simpson(fx, -10, 10, 100))
print(my_simpson(fx, -10, 10, 1000))
print(integrate.quad(fx, -10, 10))