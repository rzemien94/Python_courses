# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:24:09 2022

@author: rzemi
"""

for i in range(10,0,-1):
    print(i)
    
list=list(range(10))
print('List:',list,type(list),id(list))

list2=list[:]
print('List:',list2,type(list2),id(list2))

print(list[-1::-1])