# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:13:59 2022

@author: rzemi
"""

s="A Python script"

print(s[2:8])

print(s[:8])
print(s[8:])

message='Document "cv.doc" was printed on printer: XEROX'
print(message)

print(message.find(':'))
print(message[message.find(':')+2:])

message1=message[message.find('"')+1:]
message1=message1[:message1.find('"')]
print(message1)

 