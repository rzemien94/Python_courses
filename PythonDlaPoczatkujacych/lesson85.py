# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:27:30 2022

@author: rzemi
"""

i=0
imax=50
previous=0

while i < imax:
    print(previous+i)
    previous=i
    i+=1
    
import random
my_number=random.randint(0, 20)

guess=-1

trials=1

while guess != my_number:
    guess=int(input())
    if guess == my_number:
        print("congratulations, you wan after",trials,"trials")
    else:
        print("soory try again")
    trials+=10
    