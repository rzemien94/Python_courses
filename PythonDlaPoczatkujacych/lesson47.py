# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:40:27 2022

@author: rzemi
"""

name='Mateusz'
age=27
daysInYear=365
message='%s is %d years old, so is about %d days old'
print(message % (name,age,daysInYear*age))

message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,daysInYear*age))

print(message.format('chris',17,daysInYear*17))

print(1234567890//12345)
print(1234567890%12345)

print('1234567890 devided by 12345 is',1234567890//12345,'and the rest is',1234567890%12345)