# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:26:22 2020

@author: Omar Abdelaal
"""

import numpy as np

#defining the lehmer function
def lehmer(n):
  a = np.ones([n,n])
  
  for i in range(n):
    for j in range(n):
      if j>=i:
        a[i,j] = (i+1)/(j+1)
      elif i>j:
        a[i,j] = (j+1)/(i+1)
  return a

#printing out the result
print(lehmer(3))
print(lehmer(5))
print(lehmer(6))