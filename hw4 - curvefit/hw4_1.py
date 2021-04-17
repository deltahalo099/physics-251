# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:32:42 2020

@author: Omar Abdelaal
"""
#importing our tools...
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#collecting the data from ASCII file
data_10 = 'data/dat_10.txt'
data_11 = 'data/dat_11.txt'
data_12 = 'data/dat_12.txt'

data1 = np.genfromtxt(data_10, skip_header=1)
data2 = np.genfromtxt(data_11, skip_header=1)
data3 = np.genfromtxt(data_12, skip_header=1)

#splitting the columns into single arrays
x1 = data1[:,0]
y1 = data1[:,1]

x2 = data2[:,0]
y2 = data2[:,1]

x3 = data3[:,0]
y3 = data3[:,1]

#plotting our data
plt.plot(x1, y1, '.', label = 'data 1')

"""
plt.plot(x2, y2, '.', label = 'data 2')
plt.plot(x3, y3, '.', label = 'data 3')
"""
         
plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.grid()
plt.legend()


#defining the regression function
n = x1.size

def slope(x, y):
  c1, c2, c3, c4 = 0, 0, 0, 0
  for i in range(n):
    c1 += x[i]*y[i]
    c2 += x[i]
    c3 += y[i]
    c4 += x[i]**2
 
  m = ((n*c1) - (c2*c3))/(n*c4)-(c2**2)
  return m


def intercept(x, y):
  c1, c2, c3, c4 = 0, 0, 0, 0
  for i in range(n):
    c1 += x[i]**2
    c2 += y[i]
    c3 += x[i]*y[i]
    c4 += x[i]

  b = ((c1*c2) - (c3*c4))/((n*c1) - (c4**2))
  return b


def R2(x, y):
  def mean(x):
    s = 0
    for i in range(n):
      s += y[i]
    mean = s/n
    return mean
    
  def yh(x):
    yh = slope(x, y)*x[i] + intercept(x, y)
    return yh 
  
  numerator = 0
  denominator = 0
  for i in range(n):
    numerator += (yh(x) - x[i])**2
    denominator += (mean(y) - x[i])**2
    
  R_2 = 1 - (numerator/denominator)
  return R_2


regression = slope(x1, y1)*x1 + intercept(x1, y1)
plt.plot(regression)

print(slope(x1, y1))
print(intercept(x1, y1))
print(R2(x1, y1))

def line(x, m, b):
  why = m*x + b
  return why

popt0, pcov0 = curve_fit(line, x1, y1)

b = popt0[0]
m = popt0[1]
curve = m*x1 + b
plt.plot(curve)
