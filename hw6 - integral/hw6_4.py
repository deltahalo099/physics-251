# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:19:09 2020

@author: Omar Abdelaal
"""

def f1(x):
    y = ((x**3)/81) + 1
    return y

#trapeziodal method
def my_trap(myf, a, b, n):
    dx = (b-a)/n
    
    xi = a
    A = 0.0
    for i in range(n):
        xip1 = xi + dx
        A = A + myf(xi) + myf(xip1)
        xi = xip1
    
    A = A * dx/2.0
    return A

#simpsons method
def my_simpson(myf, a, b, n):
    dx = (b-a)/n
    
    xi = a
    A = 0.0
    for i in range(n):
        xip1 = xi + dx
        ximid = (xi + xip1)/2.0
        A = A + myf(xi) + 4.0*myf(ximid) + myf(xip1)
        xi = xip1
    
    A = A * dx/6.0
    return A

#integrating and comparing 2 areas
a_exact = 4.79
a_trap = my_trap(f1, 0, 4, 2)
a_simp = my_simpson(f1, 0, 4, 2)

dA = abs((a_trap - a_simp)/a_simp)

print('a_exat = {} \na_trap = {} \na_simp = {} \ndA = {}'.format(a_exact, a_trap, a_simp, dA))

#trapezoids dA < 10^-2
while dA < 10e-2:
    n = 1
    a_trap = my_trap(f1, 0, 4, n)
    dA = abs((a_trap - a_simp)/a_simp)
    n += n + 1
    print(n)