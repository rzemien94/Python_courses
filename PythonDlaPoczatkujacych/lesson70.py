# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:22:57 2022

@author: rzemi
"""

minLieks=500
minShares=100

likes=1300
shares=100

if likes >= minLieks and shares >= minShares:
    print("tak")
else:
    print("nie")
    
isPizzaOrdered=False
isBigDrinkOrdered=False
isWeekend=False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("tak")
else:
    print("nie")
    
diskSize=14
diskSizeUsed=133
fileSize=7

if diskSize >= (diskSizeUsed + fileSize):
    print("File can be downloaded")
else:
    print("Disk size is too small")