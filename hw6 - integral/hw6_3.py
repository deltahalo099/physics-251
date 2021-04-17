# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:23:48 2020

@author: Omar Abdelaal
"""

import numpy as np
from scipy import integrate

#functions to integrate
def f1(x):
    y = x**4
    return y

def f2(x):
    y = 2/(x-4)
    return y

def f3(x):
    y = x**2 * np.log(x)
    return y

def f4(x):
    y = np.exp(2*x)*np.sin(2*x)
    return y

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

#lets integrate!
n = np.array([1, 10, 100, 1000])

#function 1
print('f1:')
for i in range(n.size):
    approx = my_simpson(f1, 0, 4, n[i])
    print('n= {} approx = {}'.format(n[i], approx))
    
print(integrate.quad(f1, 0, 4))

    
#function 2
print('\nf2:')
for i in range(n.size):
    approx = my_simpson(f2, 0, 3, n[i])
    print('n= {} approx = {}'.format(n[i], approx))
    
print(integrate.quad(f2, 0, 3))
    
#function 3
print('\nf3:')
for i in range(n.size):
    approx = my_simpson(f3, 1, 4, n[i])
    print('n= {} approx = {}'.format(n[i], approx))

print(integrate.quad(f3, 1, 4))

#function 4
print('\nf4:')
for i in range(n.size):
    approx = my_simpson(f4, 0, 2*np.pi, n[i])
    print('n= {} approx = {}'.format(n[i], approx))
    
print(integrate.quad(f4, 0, 2*np.pi))