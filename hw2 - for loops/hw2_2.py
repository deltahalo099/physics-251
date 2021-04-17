# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 07:19:51 2020

@author: Omar Abdelaal
"""

import numpy as np

#creates array of 100 elements
a = np.ones(100)

#populates array from 1 - 100
for i in range(0, 100):
    a[i] = i + 1

#print odd values between 40 - 60
for i in range(40, 60, 2):
    print(a[i])