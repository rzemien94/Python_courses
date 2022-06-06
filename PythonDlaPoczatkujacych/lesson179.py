# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 08:25:27 2022

@author: rzemi
"""
import sys

tasksPerPerson=0
try:
    tasks=32
    personStr=input("How many persons are there in the team?")
    persons=int(personStr)
    
    #print ('this is a message")
    
    tasksPerPerson=tasks/persons
except:
    print("Something went wrong...",sys.exc_info()[0])
print("Every person should have arround",tasksPerPerson,"tasks")