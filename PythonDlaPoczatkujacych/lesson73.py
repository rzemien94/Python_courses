# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:40:05 2022

@author: rzemi
"""
minLikes=500
minShares=100

likes=1
shares=101

if likes < minLikes:
    print("lack of likes")
elif shares < minShares:
    print("Lack of shares")
else:
    print("ok")
    
isPizzaOrdered=False
isBigDrinkOrdered=True
isWeekend=False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("tak")
elif not isPizzaOrdered and not isBigDrinkOrdered:
    print("nie zamowiono pizzy ani duzego napoju")
elif isWeekend:
    print("is weekend")