# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:40:43 2022

@author: rzemi
"""

def WeekDayInFranch(dayNumber):
    names={
        0: "lundi",
        1: "madi",
        2: "drugi",
        3: "trzeci",
        4: "czw",
        5: "pt",
        6: "sob"
    }
    
    return names.get(dayNumber,"error")

print(WeekDayInFranch(2))
print(WeekDayInFranch(8))
