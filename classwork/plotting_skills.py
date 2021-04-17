# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:33:34 2020

@author: Ziron
"""

#(x^2 + y^2)^2 = a*x^2*y

import matplotlib.pyplot as plt
import numpy as np

a = 3.0
theta = np.linspace(0, np.pi, 100)

x = a * np.cos(theta)**3 * np.sin(theta)

y = a * np.cos(theta)**2 * np.sin(theta)**2

plt.plot(x, y, '.-')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')