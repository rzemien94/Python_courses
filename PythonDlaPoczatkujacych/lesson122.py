# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 18:10:53 2022

@author: rzemi
"""

import random

min=1
max=6

dice=random.randint(min, max)

print(dice)

if dice == 1:
    print(" o ")
elif dice == 2:
    print("  o")
    print("  ")
    print("o  ")
elif dice == 3:
    print("  o")
    print(" o ")
    print("o  ")
elif dice == 4:
    print("o o")
    print("  ")
    print("o o")
elif dice == 5:
    print("o o")
    print(" o ")
    print("o o")
elif dice == 6:
    print("oo")
    print("oo")
    print("oo")
    
dices=[]

for i in range(5):
    dices.append(random.randint(min, max))

dices.sort()
print(dices)    