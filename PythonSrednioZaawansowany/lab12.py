# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:02:11 2022

@author: rzemi
"""

import os

path=r'F:\Users\rzemi\Desktop\KursyPython\PythonSrednioZaawansowany\data.txt'

os.remove(path)

if os.path.isfile(path):
    print('File %s exist' % path)
else:
    print('creating a file %s' % path)
    open(path,'x').close()
    print('File %s created' % path)