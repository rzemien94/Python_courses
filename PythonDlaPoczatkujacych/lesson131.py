# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:26:09 2022

@author: rzemi
"""

import datetime

print(datetime.MINYEAR,datetime.MAXYEAR)

d1=datetime.timedelta(days=1,hours=2,minutes=-30)

print(d1)

d2=datetime.timedelta(days=-1,hours=-2,minutes=-3)

print(d2)

print(d1+d2)

print(datetime.date.today())

today=datetime.date.today()
daysToPay=datetime.timedelta(days=7)
print(today)
print(daysToPay.days)
print(today+daysToPay)

endOfTheWorld=datetime.date.max

print(endOfTheWorld)

print(endOfTheWorld.day)

bornDate=datetime.date(1994,4,22)
today=datetime.date.today()

print(today-bornDate)

print(datetime.datetime.now())

print(datetime.datetime.today())

print(datetime.datetime.utcnow())

print(datetime.datetime.today().weekday())

print("%a",datetime.datetime.now().strftime("%a"))

print("%A",datetime.datetime.now().strftime("%A"))
