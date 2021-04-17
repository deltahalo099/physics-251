# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:49:12 2020

@author: Ziron
"""

import numpy as np

a = np.array([1,3,5,7])
b = np.array([1,2,3,4])
c = a.dot(b)

print('a{} . b{} = c{}'.format(a, b, c))

d = np.array([[1],[2],[3]])

print(d.T)

x = np.zeros((10,10), dtype=int)
print(x)