# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 18:45:19 2022

@author: rzemi
"""

import time

print(time.time())

print(time.localtime(time.time()))

import calendar

print(calendar.month(2022,4))

calendar.setfirstweekday(6)

print(calendar.month(2022,4))

print(calendar.isleap(2000))



