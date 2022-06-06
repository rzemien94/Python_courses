# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:11:51 2022

@author: rzemi
"""

import datetime

def DaysToEndOfYear(year=datetime.datetime.today().year,month=datetime.datetime.today().month,day=datetime.datetime.today().day):
    #today=datetime.datetime.today()
    today=datetime.datetime(year,month,day)
    daysOfYear=today.strftime('%j')
    lastDayOfYear= datetime.datetime(today.year, 12, 31)
    daysOfLastYear=lastDayOfYear.strftime('%j')
    daysToEnd=int(daysOfLastYear)-int(daysOfYear)
    
    #print("to the ond of the year is:",daysToEnd,"days")
    
    return daysToEnd


DaysToEndOfYear(2022,12,20)

DaysToEndOfYear(2022,day=12,month=2)

DaysToEndOfYear()

print("to the ond of the year remaind:",DaysToEndOfYear(), "days")

days=DaysToEndOfYear(2000,1,10)
print("to the ond of the year remaind:",days, "days")