# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:34:45 2022

@author: rzemi
"""

countries=['fr','us','de','ru']
countries[1]='gb'
print(countries[1])

countries.append('pl')
print(countries)

countries.insert(2, 'es')
print(countries)

countries.remove('ru')
print(countries)

countries.sort()
print(countries)

countries.reverse()
print(countries)

print(countries.pop(2))
print(countries)

print(countries.index('pl'))
print(countries)

print(countries.count('de'))
newList=['fi','se']
countries.extend(newList)
countriesCopy=countries.copy()
countriesCopy.clear()
print(countries)
print(countriesCopy)