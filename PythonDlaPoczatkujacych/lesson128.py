# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 18:29:20 2022

@author: rzemi
"""
'''
import time
 
# sprawdzenie wersji pythona
import sys
print(sys.version)
 
# zamiast
#print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
print(time.perf_counter(), time.localtime(time.perf_counter()))
'''

import time

print(time.time())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

print(time.localtime(time.perf_counter()))

import calendar

print(calendar.month(2017,9,w=5,l=2))
print(calendar.month(2017,9))
print(calendar.weekday(2017,9,29))
calendar.setfirstweekday(6)
print(calendar.month(2017,9))
print(calendar.weekday(2017,9,29))

print(calendar.isleap(2021))

print(calendar.leapdays(2000, 2022))

print(calendar.calendar(2022))

