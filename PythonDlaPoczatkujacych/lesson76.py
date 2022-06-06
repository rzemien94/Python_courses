# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:50:42 2022

@author: rzemi
"""

musclePain =False
fever=True
weakness =True
isMan=True

print("suspicion of influenza" if musclePain and fever and weakness else "The flu is unlikely")

if musclePain and fever and weakness:
    print("suspicion of influenza")
elif weakness and (not fever and not musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")
    
    
if (musclePain and fever and weakness) or (isMan and (musclePain or fever or weakness)):
    print("suspicion of influenza")
elif weakness and (not fever and not musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")
    
isCheckCompleted = False
 
print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")