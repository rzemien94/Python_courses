# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:21:34 2022

@author: rzemi
"""

quote='A good programmer is someone who always looks both ways before crossing a one-way street'
print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.isupper())
print(quote.find('one'))
print(quote.replace('one', '1'))
print(quote.replace('one', '1').replace('both', '2'))
print(quote.split(' '))
print(quote.isdecimal())
print(quote.isdigit())
print(quote.isalpha())
print(quote.isalnum())