# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:26:41 2022

@author: rzemi
"""

x=['load data', 'export data', 'analyze & predict']
print("opcje do wyboru:",x)
choice=input('wybierz numer opcji (0,1,2):')

while choice:
    if choice.isdigit():
        if int(choice) >= 0 and int(choice) < len(x):
            print('wybrana opcja nr:',int(choice),'opcja:',x[int(choice)])
            choice=input('wybierz numer opcji (1,2,3):')
        else:
            print('niedopuszczalna opcja')
            choice=input('wybierz numer opcji (1,2,3):')
    else:
        print('wybor nieprawidlowy')
        choice=input('wybierz numer opcji (1,2,3):')



