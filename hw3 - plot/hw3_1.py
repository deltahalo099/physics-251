# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:32:32 2020

@author: Ziron
"""

import math
import matplotlib.pyplot as plt
import numpy as np

#creates domain from -pi to pi divided into 50 units
r = np.linspace(-math.pi, math.pi, 50)

#3 seperate functions
f1 = np.cos(2*r)
f2 = 2*((np.cos(r-1))**2)
f3 = 1/(np.cos(r)) + np.tan(r)

#graph labels and title
plt.grid()
plt.title('Problem 1')
plt.xlabel('-pi to pi')
plt.ylabel('f(x)')

#plot the functions
plt.plot(f1)
plt.plot(f2)
plt.plot(f3)