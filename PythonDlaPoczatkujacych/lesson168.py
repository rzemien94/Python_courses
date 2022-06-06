# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:48:15 2022

@author: rzemi
"""

import os
import time

dir=input("path to a dir:")

if os.path.exists(dir) == False:
    print("the dir does not exist")
else:
    file=input("filename:")
    path=os.path.join(dir, file)
    if os.path.exists(path) == False:
        print("the file does not exist")
    else:
        print("properties of the file:")
        print(time.localtime(os.path.getmtime(path)))
        print(os.getcwd())
        print(os.path.relpath(path))