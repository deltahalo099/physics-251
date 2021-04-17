# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:01:25 2020

@author: Omar Abdelaal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#imported the data
harmonic_data = 'harmonic_motion.csv'
data = np.genfromtxt(harmonic_data, delimiter=',', skip_header=1)

#seperated the data by column
time = data[:, 0]
pos = data[:, 1]
vel = data[:, 2]

#defined our model
def model(t, a, al, w, b, g):
  y = a*np.exp(-al*t)*np.cos(w*t+b)+g
  return y

#set up our curve_fit with initial guesses
popt0, pcov0 = curve_fit(model, time, pos, p0=(0.5, -.01, 2*np.pi, 0.0, 0.1))

#produced graph (missing the graphed regression)
plt.title('harmonic motion')
plt.plot(time, pos)
plt.xlabel('time')
plt.ylabel('position')
plt.grid()
plt.legen()
