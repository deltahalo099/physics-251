# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:26:40 2020

@author: Omar Abdelaal
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.array([90, 95, 100])
z = np.array([20, 22, 33])

ai = 99.5
zi = np.interp(ai, a, z)

plt.plot(a, z, '.')
print(zi)

