# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:45:46 2022

@author: rzemi
"""

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flights=[(start,dest) for start in ports for dest in ports]
#print(flights)
print(len(flights))

flights=[(start,dest) for start in ports for dest in ports if start!=dest]
#print(flights)
print(len(flights))

flights=[(start,dest) for start in ports for dest in ports if start<dest]
#print(flights)
print(len(flights))