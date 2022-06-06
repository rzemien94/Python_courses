# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:02:06 2022

@author: rzemi
"""

countryLeaders={'PL':'Duda','US':'Trump'}
countryLeaders['DE']='Merkel'
'''
print(countryLeaders)

print(countryLeaders['US'])

countryLeaders['DE']='Merkel'
s
print('-----------------')
print(countryLeaders.keys())
print('-----------------')
print(countryLeaders.values())
print('-----------------')
print(countryLeaders.items())
print('-----------------')
'''
#print(countryLeaders.popitem())

#print(countryLeaders.setdefault('FR','Macron'))

#print(countryLeaders.get('RU'))

newleders={'RU':'Putin','DE':'Schulz'}
print(newleders)
countryLeaders.update(newleders)

print(countryLeaders)