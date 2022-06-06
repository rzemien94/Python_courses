# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 08:41:18 2022

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
    
except ValueError as e:
    print("sorry - you need to enter an int number:",e)
except ZeroDivisionError as e:
    print("sorry - you the number must be greater than 0",e)
except:
    print("Something went wrong...",sys.exc_info()[0])

else:
    print("Every person should have arround",tasksPerPerson,"tasks")

finally:
    print("script finished")