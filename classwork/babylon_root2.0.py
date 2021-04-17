# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:34:08 2020

@author: Ziron
"""


import numpy as np

def root2 (x):
  
  epsilon = 1.0e-3 #stopping
  y1 = x
  y2 = .5 * (y1 + x/y1)
  
  while abs(y2 - y1) > epsilon:
    y1 = y2
    y2 = .5 * (y1 + x/y1)
    
  return y2

x = float(input('enter x = '))
y = root2(x)

print('sqrt of x = {}'.format(y))