# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:00:16 2020

@author: Ziron
"""

import numpy as np

fname = 'sinusoidal_data.csv'
data01 = np.genfromtxt(fname, delimiter=',', skip_header=1)

t = data01[:,0]
y = data01[:,1]

print(data01)