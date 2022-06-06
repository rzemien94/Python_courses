# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:27:43 2022

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

def generate_values(func,*args):
    for i in args:
        print(func(i))

x_table = list(range(11))
 
print(generate_values(double, *x_table))
print(generate_values(square, *x_table))
print(generate_values(negative, *x_table))
print(generate_values(div2, *x_table))
        