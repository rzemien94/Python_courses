# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:55:39 2022

@author: rzemi
"""

def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2

number=8

transformation=[double,square,div2,negative]
tmp_return_value=number

for i in transformation:
    tmp_return_value=i(tmp_return_value)
    print(tmp_return_value)
    
transformation=[square,square,div2,double]
tmp_return_value=number

for i in transformation:
    tmp_return_value=i(tmp_return_value)
    print(tmp_return_value)