# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:47:07 2020

@author: Omar Abdelaal
"""
import numpy as np
import matplotlib.pyplot as plt

def my_left_rect(myf, a, b, n):
    
    dx = (b-a)/n
    xi = a
    A = 0.0
    
    for i in range(n):
        A = A + myf(xi)
        xi = xi + dx
    A = A*dx
    return A

#functions
def f1(x):
    y = x/4 + 1
    return y

def f2(x):
    y = np.sin(x)/x
    return y
    
a = 0.0
b = 4.0
n = 2

A = my_left_rect(f1, a, b, n)
print('A_est = {}'.format(A))

a = 0.1
b = 19.0 * np.pi
M = 1000

A = np.zeros(M-1)
for i in range(1, M):
    A[i-1] = my_left_rect(f2, a, b, i)


plt.plot(A, '.')
plt.grid()