# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:12:20 2022

@author: rzemi
"""

days = ['mon','tue','wed','thu','fri','sat','sun']

workdays=days.copy()

workdays.remove('sat')
workdays.remove('sun')

print(days,workdays)