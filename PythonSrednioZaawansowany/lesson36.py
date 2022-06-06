# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:47:36 2022

@author: rzemi
"""

var_x=10
password='secret'
source='33+3'

#globals=globals().copy()
#del globals['password']
globals={}

resoult=eval(source, globals)
print(resoult)

#print(globals())