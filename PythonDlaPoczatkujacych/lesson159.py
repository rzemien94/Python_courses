# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:28:19 2022

@author: rzemi
"""

import datetime

def DaysToEndOfYear(*dates):
    for today in dates:
        #today=datetime.datetime.today()
        #today=datetime.date(year,month,day)
        daysOfYear=today.strftime('%j')
        lastDayOfYear= datetime.datetime(today.year, 12, 31)
        daysOfLastYear=lastDayOfYear.strftime('%j')
        daysToEnd=int(daysOfLastYear)-int(daysOfYear)
        
        print("to the ond of the year is:",daysToEnd,"days")
    
    return 


DaysToEndOfYear(datetime.date(1999,1,15))
DaysToEndOfYear(datetime.date(1999,1,15),datetime.date(1999,8,15))
DaysToEndOfYear(datetime.date(1999,1,15),datetime.date(1999,8,15),datetime.datetime.today())