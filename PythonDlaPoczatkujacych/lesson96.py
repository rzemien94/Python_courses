# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:19:31 2022

@author: rzemi
"""

for x in range(1,6):
    line=str(x)
    for y in range (1,6):
        line+='\t%3d' %(x*y)
    print(line)