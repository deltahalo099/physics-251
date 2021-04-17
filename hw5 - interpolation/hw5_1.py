# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:54:48 2020

@author: Omar Abdelaal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#importing and arranging data

data = np.genfromtxt('velocity_run18.txt', skip_header=1)

t = data[:,0]   #time
v = data[:,1]   #velocity
dv = data[:,2]  #uncertainty
n = t.size      #size of array
ni = n-1        #interpolation values

tint = np.zeros(ni) # midpoint values
vint = np.zeros(ni) # interpolated values

#creating our interpolation function

#y_i = y_1 + (x_i - x_1)(y_2 - y_1)/(x_2 - x_1)

def interpolation(xi, x1, y1, x2, y2):
    yi = y1 + (xi - x1)*(y2 - y1)/(x2 - x1)
    return yi
  
#collecting interpolation data
for i in range(ni):
    thalf = (t[i+1]+t[i])/2.0
    vhalf = interpolation(thalf, t[i], v[i], t[i+1], v[i+1])
    tint[i] = thalf
    vint[i] = vhalf
    
#curve fit
def line(x, m, b):
  y = m*x + b
  return y

popt0, pcov0 = curve_fit(line, t, v, sigma=dv)
print(popt0)
  
#PLOTS
#raw and interpolated data + error
plt.figure()
plt.title('raw data + error')
plt.plot(t,v,'.r', label="raw data")
plt.errorbar(t, v, yerr=dv, fmt='.',capsize=3, ecolor='r',label='Uncertainty')

plt.xlabel('time')
plt.ylabel('velocity')
plt.grid()
plt.legend()

#interpolated data
plt.figure()
plt.title('interpolated data')
plt.plot(tint, vint, '.k', label="interpolated")
plt.xlabel('time interpolated')
plt.ylabel('velocity interpolated')
plt.grid()
plt.legend()

#curve fit
m = popt0[0]
b = popt0[1]
yfit = m*t+b

plt.figure()
plt.title('curve fit')
plt.plot(t, yfit, label="curve_fit")
plt.plot(t,v,'.r', label="raw data")
plt.xlabel('time')
plt.ylabel('velocity')
plt.grid()
plt.legend()