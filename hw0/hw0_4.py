# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:52:17 2020

@author: Ziron
"""

import numpy as np

a = np.zeros((3, 3))
b = np.zeros((3, 3))

print('a.ij = 1 b.ij = 1\n')

for i in range(0, 3):
  for j in range(0, 3):
     a[i][j] = 1
     b[i][j] = 1

c1 = a.dot(b)
c2 = b.dot(a)
c3 = (a.transpose()).dot(b)
c4 = a.dot(b.transpose())
c5 = c1.transpose()

print('ab')
print(c1)

print('ba')
print(c2)

print('aTb')
print(c3)

print('abT')
print(c4)

print('(ab)T')
print(c5)
  

#--------------------------------