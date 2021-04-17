# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 08:10:45 2020

@author: Omar Abdelaal
"""

import numpy as np
import random

#generate 10 x 10 matrix
a = np.zeros([10, 10])

#iterate through columns and rows
for i in range(10):
    for j in range(10):
        a[i][j]= random.randint(7, 10)

print(a)
    
#print third column and third row
print('the third column:')
print(a[:,2])

print('the third row:')
print(a[2,:])

#replace column 10 with 99
for i in range(10):  
    a[i][9] = 99
  
b = np.copy(a)
print(b)


#checks if element i,j is 8 then replaces with -1
for i in range(10):
  for j in range(10):
    if a[i][j] == 8:
      a[i][j] = -1
      
c = np.copy(a)
print(a)