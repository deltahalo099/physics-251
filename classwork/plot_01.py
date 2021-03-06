# -*- coding: utf-8 -*-
"""
===============================================================================

-------------------------------------------------------------------------------
Created on Thu Feb 14 10:24:20 2019
@author: Fernando Camelli
===============================================================================
"""
# =============================================================================
# GLOBAL VAR - GLOBAL MODS
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# END GLOBAL VAR - GLOBAL MODS
# =============================================================================


# =============================================================================
# FUNCTIONS
# -----------------------------------------------------------------------------
def f(x):
    y = 2.0 * np.cos(x)**2 - 1.0
    return y

def g(x):
    y = np.exp(0.001 * x) + np.log( x**2 )
    return y

# -----------------------------------------------------------------------------
# END FUNCTIONS
# =============================================================================


# =============================================================================
# MAIN SCRIPT
# -----------------------------------------------------------------------------
xmin = -10.0
xmax = 10.0
dx = 0.01

n = int((xmax-xmin)/dx)+1
    
x = np.linspace(xmin,xmax,num=n)

yf = f(x)

plt.figure(1)
plt.plot(x,yf,'-',label='f(x)')



yg = g(x)

plt.plot(x,yg,'-',label='g(x)')

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.savefig('g.png',dpi=200)

# -----------------------------------------------------------------------------
# END MAIN SCRIPT
# =============================================================================
