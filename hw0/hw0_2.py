# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 06:57:48 2020

@author: Omar Abdelaal
"""

n = range(1, 10001)

#Problem 1
total_1 = 0

for i in n:
    total_1 = total_1 + (1/(i))  
    
#Problem 2
total_2 = 0

for i in n:
    total_2 = total_2 + (1/(i**i))
    
#Problem 3
total_3 = 0

for i in n:
    total_3 = total_3 + (-1**i)/(i)
    
#Problem 4
total_4 = 0

for i in n:
    total_4 = total_4 + (-1**i)/(i**2)





#final answers
print('Answer 1 = ' + str(total_1))
print('Answer 2 = ' + str(total_2))
print('Answer 3 = ' + str(total_3))
print('Answer 4 = ' + str(total_4))