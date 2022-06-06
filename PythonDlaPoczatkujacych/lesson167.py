# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:28:20 2022

@author: rzemi
"""

import os
import time

print(os.getcwd())

currDir=os.getcwd()

filename='result.txt'
fullpath=os.path.join(currDir, filename)

print(fullpath)

relativePath='output.txt'

print(os.path.abspath(relativePath))
print("----------------------")
filepath=r'c:\tmp\results.txt'
print(os.path.basename(filepath))
print(os.path.dirname(filepath))

print(os.path.exists(filepath))
