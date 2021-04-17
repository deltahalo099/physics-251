# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:12:14 2020

@author: Ziron
"""

import numpy as np
import random

"""
this was an experiment to see how to execute a function
on every element of an array
basically the arguments of the function can be anything
in the body of the function treat the parameter you want as an array
as if it were one. hence the y[i] in the body of f(y)
"""
x = np.zeros(10)
print(x)

def f(y):
  for i in range(x.size):
    y[i] = random.randint(1,6)
  return y
  
print(f(x))