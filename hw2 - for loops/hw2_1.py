# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 07:08:25 2020

@author: Omar Abdelaal
"""

#Geometric series

#n = 5
n = 10
#n = 100
#n = 200
#n = 500

x = 0
for i in range(0, n+1):
    x += 1/(2**i)

print(x)
    
x = 0
for i in range(2, n+1):
    x += 4/(3**i)
    
print(x)
    
x = 0
for i in range(1, n+1):
    x += (3/(2**i) - 2/(5**i))

print(x)