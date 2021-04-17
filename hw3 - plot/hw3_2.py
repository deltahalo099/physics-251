# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:31:46 2020

@author: Ziron
"""
import math
import numpy as np
import matplotlib.pyplot as plt


r = np.linspace(-4, 4, 100)
x = np.linspace(-6, 6, 100)
y = np.linspace(1, 6, 100)


#part 1
def f1a(r):
    f1a = np.sin(r)
    return f1a

def f1b(r):
    f1b = r**2
    return f1b
        
f1a, = plt.plot(f1a(r), label = 'function 1a')
f1b, = plt.plot(f1b(r), label = 'function 1b')

plt.legend(handles = [f1a, f1b])
plt.title('problem 2-1')
plt.grid()


#part 2
def f2a(r):
    f2a = np.sin(2*r)
    return f2a

def f2b(r):
    f2b = ((r**3)/10) + ((r**2)/10)
    return f2b

f2a, = plt.plot(f2a(r), label = 'function 2a')
f2b, = plt.plot(f2b(r), label = 'function 2b')

plt.legend(handles = [f2a, f2b])
plt.title('problem 2-2')
plt.grid()


#part 3
def f3a(x):
    f3a = (np.exp(.001*x) + np.log(x**3))
    return f3a
    
def f3b(x):
    f3b = (0.1*(x**3)) + (0.1*(x**2)) - 5
    return f3b

f3a, = plt.plot(f3a(x), label = "function 3a")
f3b, = plt.plot(f3b(x), label = "function 3b")

plt.legend(handles = [f3a, f3b])
plt.title('problem 2-3')
plt.grid()
