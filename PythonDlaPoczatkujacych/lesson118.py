# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:46:30 2022

@author: rzemi
"""

import random

print(random.randint(1, 100))

print(random.choice(range(1,100)))

print(random.randrange(1,100))

list=['a','scsa','as','sda','sdfd']

random.shuffle(list)

print(list)

print(random.random())