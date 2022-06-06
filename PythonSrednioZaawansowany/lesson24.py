# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:51:59 2022

@author: rzemi
"""

workDays=[19,21,22,22,21,20,22]

print(workDays)

print(workDays[2])

enumerateDays=list(enumerate(workDays))
print(enumerateDays)

for pos, value in enumerateDays:
    print('Position ',pos,'value ',value)
    
months=['I','II','III','IV','V','VI','VII']

monthsDays=list(zip(months,workDays))
print(monthsDays)

for pos, value in monthsDays:
    print('Months ',pos,'value ',value)
    
for pos, (m,d) in enumerate(zip(months,workDays)):
    print(pos,m,d)
    