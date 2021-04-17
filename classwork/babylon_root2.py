# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:34:08 2020

@author: Ziron
"""


import numpy as np

def root2 (x):
  #y = x
  n = 10
  y = np.empty(n)
  y[0] = x
  
  for i in range(1, n):
    y[i] = 0.5 * (y[i-1]+x/y[i-1])
  return y

x = float(input('enter x = '))
y = root2(x)

print('sqrt of x = {}'.format(y))