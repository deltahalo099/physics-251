# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:32:32 2020

@author: Ziron
"""

import numpy as np

n = int(input('what size square matrix would you like?'))
a = np.zeros([n,n])

c = int((n-1)/2)



for i in range(n):
  a[i][n-i-1] = 1
  a[i][i]     = (i+1)**2

print(a)

b = np.copy(a)
for i in range(n):
  b[i] = 6
  
print(b)