# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:24:45 2022

@author: rzemi
"""
import random

health=50
difficulty=3
potion_health=int(random.randint(25, 50) / difficulty)

health=health+potion_health
print(health)
