# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:46:59 2022

@author: rzemi
"""

isWeekend=True
print('is weekend=',isWeekend)

temp=22
print('Temperature=',temp)

toDoList=''
print('ToDoList=',toDoList)

isHappy=isWeekend and temp >=20 and toDoList == ''

print('isHappy',isHappy)

isHappy1= not isWeekend and temp<20 and toDoList != ''
print('isHappy1',isHappy1)

isHappy2=isHappy or isHappy1
print('isHappy2',isHappy2)
