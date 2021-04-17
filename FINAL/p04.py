# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:28:57 2020

@author: Omar Abdelaal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.genfromtxt('data_p04.csv', delimiter=",", skip_header=1)

x =  data[:,0]
y =  data[:,1]
dy = data[:,2]

def fx(x, y0, m, A, u, s):
    y = y0 - m*x + A*np.exp(-((x-u)**2)/2*s**2)
    return y

#initial guesses
y0_g = 4
m_g = 1
A_g = 5
u_g = 45
s_g = 1

guess = np.array([y0_g, m_g, A_g, u_g, s_g])

popt0, pcov0 = curve_fit(fx, x, y, p0=guess)
print(popt0)

y0 = popt0[0]
m =  popt0[1]
A =  popt0[2]
u =  popt0[3]
s =  popt0[4]

fit = fx(x, y0, m, A, u, s)


#plot of raw data and curve_fit
plt.figure()
plt.plot(x, fit, label="curve_fit")
plt.plot(x, y, label="raw data")
plt.errorbar(x, y, yerr=dy, fmt='o')
plt.legend()