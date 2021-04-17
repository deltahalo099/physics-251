# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:02:12 2020

@author: Omar Abdelaal
"""

n = range(1001)

#Problem 1
total_1 = 0

for i in n:
    total_1 = total_1 + i
    
#Problem 2
total_2 = 0

for i in n:
    total_2 = total_2 + (2*i)    
    
#Problem 3
total_3 = 0

for i in n:
    total_3 = total_3 + ((2*i) + 1)
    
#final answers
print('Answer 1 = ' + str(total_1))
print('Answer 2 = ' + str(total_2))
print('Answer 3 = ' + str(total_3))
