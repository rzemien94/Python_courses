# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:51:55 2022

@author: rzemi
"""

import random

for i in range(0,10):
    print(random.randint(1, 100))
    
number1=random.randint(1, 100)
number1bis=-1
i=0

print(number1)
while number1bis != number1:
    number1bis=random.randint(1, 100)
    i+=1
    
print("Winner after",i,"iterations")


countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
groupNumber=0
countriesLength=len(countries)

for i in range(countriesLength):
    if (i % 4) == 0:
        groupNumber+=1
        print("grupa",groupNumber)
    print(countries[i])