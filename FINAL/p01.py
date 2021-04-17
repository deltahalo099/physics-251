# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:54:42 2020

@author: Omar Abdelaal
"""

import numpy as np

#Problem 1 
#Part a

#number of elements in square matrix
n = 5
a = np.zeros([n,n])

#algorithm for defining matrix elements
for i in range(n):
    for j in range(n):
        if i == j:
            a[i,j] = 2*i + 1
        else:
            a[i,j] = i + j + 1
            
print(a)

#Part b

#number of elements in square matrix
n = 5
b = np.zeros([n,n])

#algorithm for defining matrix elements
for i in range(n):
    for j in range(n):
        if i == j:
            b[i, j] = 2
        elif (i == j + 1) or (i == j - 1):
            b[i, j] = -1
        else:
            b[i, j] = 0
            
print(b)

#Part C

c = np.zeros([n,n])
x = np.zeros([n,n])

#a function to multiply 2 matricies
def multi(a, b):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x[i, j] = a[i, k] * b[k, j]
    return x

#a function to subtract 2 matricies
def sub(x, b):
    for i in range(n):
        for j in range(n):
            c[i, j] = x[i, j] - b[i, j]
    return c

# C = A*B - C
print(sub(multi(a, b), b))