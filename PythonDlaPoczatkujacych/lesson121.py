# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 18:04:06 2022

@author: rzemi
"""
import random

for i in range (32,127):
    print(i, chr(i))
    
ints=range(33,127)
password=''

for i in range(16):
    password+=chr(random.choice(ints))
    
print(password)