# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:43:13 2020

@author: Omar Abdelaal
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#numerical integration techniques

#left rectangle method
def my_left_rect(myf, a, b, n):
    dx = (b-a)/n
    
    xi = a
    A = 0.0
    for i in range(n):
        A = A + myf(xi)
        xi = xi + dx
        
    A = A * dx
    return A

#right rectangle method
def my_right_rect(myf, a, b, n):
    dx = (b-a)/n
    
    xi = a + dx
    A = 0.0
    for i in range(n):
        A = A + myf(xi)
        xi = xi + dx
        
    A = A * dx
    return A

#trapeziodal method
def my_trap(myf, a, b, n):
    dx = (b-a)/n
    
    xi = a
    A = 0.0
    for i in range(n):
        xip1 = xi + dx
        A = A + myf(xi) + myf(xip1)
        xi = xip1
    
    A = A * dx/2.0
    return A

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

#function 1
def f1(x):
    y = x/4 + 1
