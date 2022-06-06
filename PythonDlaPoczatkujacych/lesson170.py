# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:00:26 2022

@author: rzemi
"""
import os
fileIsOk=False

while fileIsOk == False:
    filename=input("Enter path to results file: ")
    if os.path.exists(filename):
        fileIsOk=True
    else:
        print("filename does not exist, try again")
    
    
print("The results file is %s" % (filename))

