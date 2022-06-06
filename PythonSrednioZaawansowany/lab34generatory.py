# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:41:44 2022

@author: rzemi
"""

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flights=((start,dest) for start in ports for dest in ports)
#print(flights)
#print(len(flights))
i=0
while True:
    try:
        print(next(flights))
        i+=1
    except:
        print('task done len(gen)=',i)
        break

flights1=((start,dest) for start in ports for dest in ports if start!=dest)
#print(flights)
#print(len(flights1))
i=0
while True:
    try:
        print(next(flights1))
        i+=1
    except:
        print('task done len(gen)=',i)
        break

flights2=((start,dest) for start in ports for dest in ports if start<dest)
#print(flights)
#print(len(flights2))
i=0
while True:
    try:
        print(next(flights2))
        i+=1
    except:
        print('task done len(gen)=',i)
        break