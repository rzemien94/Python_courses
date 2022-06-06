# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 08:58:39 2022

@author: rzemi
"""

import os
import sys

line=input("press something info:")

path= r'F:\Users\rzemi\Desktop\KursyPython\PythonDlaPoczatkujacych\Testowe\test1.txt'

try:
    if os.path.isfile(path):
        with open(path,"a") as file:
            file.write(line)
            value=int(line)
            print("The value saved in file is:",value)
    else:
        print("file does not exist")
except FileNotFoundError as e:
    print("the folder does not exist", e)
except ValueError as e:
    print("The value entered cannot be converted to a number",e)
except:
    print("SORRY - WE HAVE AN ERROR:",sys.exc_info()[0])

else:
    print("Actions completed successfully")