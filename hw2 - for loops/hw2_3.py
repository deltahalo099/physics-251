# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 07:40:59 2020

@author: Omar Abdelaal
"""

import numpy as np

#creates array of 100 elements
a = np.ones(100)

#populates array from 1 - 100
for i in range(0, 100):
    a[i] = i + 1
    
#converts array to 10x10
x = np.reshape(a, (10, 10))
print(x)

#tranpose
print(x.transpose())