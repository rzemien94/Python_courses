# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:32:02 2022

@author: rzemi
"""

age=27
isDrunk=False
isRestictedArea=False

if age < 18:
    print("You are too young to buy alcohol")
else:
    if isDrunk:
        print("You are drunk")
    else:
        if isRestictedArea:
            print("Restricted area") 
        else:
            print('ok, you can buy alcohol')
            
print('------------------')

if age < 18:
    print("You are too young to buy alcohol")
elif isDrunk:
    print("You are drunk")
elif isRestictedArea:
    print("Restricted area")
else:
    print('ok, you can buy alcohol')
    
    