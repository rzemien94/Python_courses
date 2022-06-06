# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:54:47 2022

@author: rzemi
"""

import datetime

def DaysToEndOfYear(year,month,day):
    #today=datetime.datetime.today()
    today=datetime.datetime(year,month,day)
    daysOfYear=today.strftime('%j')
    lastDayOfYear= datetime.datetime(today.year, 12, 31)
    daysOfLastYear=lastDayOfYear.strftime('%j')
    daysToEnd=int(daysOfLastYear)-int(daysOfYear)
    
    print("to the ond of the year is:",daysToEnd,"days")
    
    return


DaysToEndOfYear(2022,12,20)

DaysToEndOfYear(2022,day=12,month=2)