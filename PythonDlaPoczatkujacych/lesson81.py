# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:11:00 2022

@author: rzemi
"""

values=[10,21,5,545,2344,1123,2151,184,2,12,1,22]

print(values)

i=0
max = len(values)-2

while i<max:
    print(i,values[i],values[i+1],values[i+2])
    if values[i]<values[i+1] and values[i+1]<values[i+2]:
        print("^--są---")
    else:
        print("nie są")
    i+=1