# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:33:36 2020

@author: Omar Abdelaal
"""

#dx/dt = 2x/t                   -> F1(x, t) = 2x / t
#dx/dt = 2x/t + 3*x**3/t**3      -> F2(x, t)
#dx/dt = -x**3 + sin t          -> F3(x, t)

def F1(x, t):
    return 2.0 * x/t

def F2(x, t):
    dxdt = 2*x / t + 3*x**2/t**3 
    return 

def F3(x, t):
    return

