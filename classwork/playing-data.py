# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:00:16 2020

@author: Ziron
"""

import csv
fname = 'sinusoidal_data.csv'
file01 = open(fname)
data01 = csv.reader(file01)

for row in data01:
  print(row)