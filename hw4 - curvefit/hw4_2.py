# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:04:00 2020

@author: Omar Abdelaal
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

sindata = 'data/sinusoidal_data.csv'
data_set = np.genfromtxt(sindata, delimiter=',')

time = data_set[:, 0]
volts = data_set[:, 1]

plt.plot(time, volts)

def v (t, a, c, w):
  v = a*np.exp(-c*t)*np.sin(w*t)
  return v

popt0, pcov0 = curve_fit(v, time, volts)
