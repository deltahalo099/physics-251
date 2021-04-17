# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:56:30 2020

@author: Ziron
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([1, 1/2, 1/3])
c = np.array([1, 1, 1])
d = np.array([-1, 2, -3])

#dot products
x = a.dot(b)
print(x)

#norm
print(np.linalg.norm(a))

