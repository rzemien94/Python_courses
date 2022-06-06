# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:40:13 2022

@author: rzemi
"""

import datetime
import math
import random

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

print(len(inputdata))
print(len(factortable))

if len(inputdata) == len(factortable):
    print("ok")
    for i in range (len(inputdata)):
        minvalue=inputdata[i]-factortable[i]*inputdata[i]
        maxvalue=inputdata[i]+factortable[i]*inputdata[i]
        print("---------1-------")
        print(minvalue)
        print(maxvalue)
        mininteger=math.floor(minvalue)
        print(mininteger)
        maxinteger=math.ceil(maxvalue)
        print(maxinteger)
        print("---------1-------")
else:
    print("inputdata and factortable need to have equal number of elements")
    

minvalue=inputdata[i]-random.random()*inputdata[i]
maxvalue=inputdata[i]+random.random()*inputdata[i]
print("--------2--------")
print(minvalue)
print(maxvalue)
mininteger=math.floor(minvalue)
print(mininteger)
maxinteger=math.ceil(maxvalue)
print(maxinteger)
print("---------2-------")

print(datetime.datetime.today())
print(datetime.datetime.today().year,"-",datetime.datetime.today().month,"-",datetime.datetime.today().day)
print(datetime.date.today().strftime("%Y-%m-%d"))