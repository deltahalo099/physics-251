# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:24:24 2020

@author: Ziron
"""

import numpy as np

#pascals triangle

n = int(input('select your n captain -'))

tri = np.zeros([n,n])

tri[0,0] = 1

for i in range(1, n):
  for j in range(n):
    tri[i,j] = tri[i-1, j-1] + tri[i-1, j]
  

print(tri)


#pascals transpose

triT = np.copy(tri)

for i in range(n):
  for j in range(n):
    triT[j, i] = tri[i, j]
  

print(triT)