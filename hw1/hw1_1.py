# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:28:13 2020

@author: Omar Abdelaal
"""

import math

#sums pi and e
real = math.pi + math.e

#converts float to scientific notation - ":.2e" specifies 2 decimal places
sci = "{:.2e}".format(real)

print(real)
print(sci)