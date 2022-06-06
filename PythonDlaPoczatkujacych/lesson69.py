# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:16:43 2022

@author: rzemi
"""

age=27

if age >= 18:
    print("You are adoult and you can buy alcohol")
else:
    print("You are too young to buy alcohol")
    
isDrunk=False

if age >= 18 and not isDrunk:
    print("You are adoult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")
    
isRestictedArea=False

if age >= 18 and not isDrunk and not isRestictedArea:
    print("You are adoult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")   
