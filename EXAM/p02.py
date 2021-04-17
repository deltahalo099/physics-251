# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:56:41 2020

@author: Omar Abdelaal
"""

import numpy as np

# x = xi + vi*t + 1/2*a*t^2

#function to determine value of t given h
def t_final(h):
  a = -9.8
  t = 0
  y = h + .5*a*t**2
  
  while y >= 0:
    t += 1

  return t

print(t_final(150))