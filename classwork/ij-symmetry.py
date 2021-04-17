# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:10:34 2020

@author: Ziron
"""

import numpy as np

n = int(input('Enter n: '))
m = int(input('Enter m: '))

a = np.empty([n,m], dtype = 'float')

for i in range(0, n):
  for j in range(0, m):
    a[i][j] = 1/(i+j+2)
    
print(a)