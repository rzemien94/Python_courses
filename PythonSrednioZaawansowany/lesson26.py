# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:13:02 2022

@author: rzemi
"""
workDays=[19,21,22,21,20,22]
months=['I','II','III','IV','V','VI']
monthDays=dict(zip(months,workDays))
print(monthDays)
for key in monthDays:
    print('key ',key,'value ',monthDays[key])
    
for value in monthDays.values():
    print('value: ',value)