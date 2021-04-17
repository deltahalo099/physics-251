# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:06:30 2020

@author: Omar Abdelaal
"""

import numpy as np
import matplotlib.pyplot as plt

#function to integrate
def fx(x):
    y = x**2
    return y

#middle rectangle method
def mid_rect(myf, a, b, n):
    dx = (b-a)/n
    
    xi = a + 0.5*dx
    A = 0.0
    for i in range(n):
        A = A + myf(xi)
        xi = xi + dx
        
    A = A * dx
    return A

#area approximations/exact value
A_exact = 1/3
A_aprx = np.zeros(100)
n = np.arange(1, 101)

for i in range(n.size):
    A_aprx[i] = mid_rect(fx, 0, 1, n[i])
    
print(A_aprx)

#difference in appoximation
dn = np.zeros(100)

for i in range(n.size):
    dn[i] = abs((A_aprx[i] - A_exact) / A_exact)
    
print(dn)

plt.plot(n, dn, label="n vs δ")
plt.legend()
plt.xlabel('n')
plt.ylabel('δ')