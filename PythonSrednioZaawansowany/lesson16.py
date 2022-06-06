# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:40:13 2022

@author: rzemi
"""

price = 123
bonus = 23
bonus_granted = True

price -= bonus if bonus_granted == True else "?"

#if bonus_granted:
 #   price -= bonus
 
print(price)


rating = 5
'''
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')
'''
print('very good') if rating ==5 else print('good') if rating == 4 else print('weak')