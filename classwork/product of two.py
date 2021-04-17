# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:23:07 2020

@author: Ziron
"""

# product of 2 matricies - n x m  * m x l
import numpy as np

c = np.zeros((10,10))
a = np.ones((10, 10))
b = np.diag((10,10))

for i in range(10):
  for j in range(10):
    for k in range(10):
      c[i,j] = c[i,j] + (a[i, k] * b[k, j])
      
print(a)
print(b)
print(c)