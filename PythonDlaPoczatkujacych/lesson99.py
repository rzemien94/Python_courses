# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:37:22 2022

@author: rzemi
"""

for candidate in range(2,31):
    
    for divider in range(2,candidate):
        
        if candidate %divider ==0:
            isPrime=False
            print("%2d is not a prime - divider is %2d" % (candidate,divider))
            break
    else:
        print("%2d is prime!" % (candidate))