# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:15:31 2022

@author: rzemi
"""

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(10):
    print(string_A)
    
for i in range(9):
    if i %2==0:
        print(string_A)
    else:
        print(string_B)
        
for i in range(9):
    print('x'*i)
    
for i in range(9):
    if i %2==0:
        print('o'*(i+1))
    else:
        print('x'*(i+1))