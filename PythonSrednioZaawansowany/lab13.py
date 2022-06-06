# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:18:58 2022

@author: rzemi
"""

import os

def CountWords(path):
    with open(path,'r') as file:
              content = file.read()
              count=len(content.split())
    return count

path= r'F:\Users\rzemi\Desktop\KursyPython\PythonSrednioZaawansowany\lab13.txt'

if os.path.isfile(path):
    print('File %s exist' % path)
else:
    print('creating a file %s' % path)
    open(path,'x').close()
    print('File %s created' % path)

print("there are {} words in the file {}".format(CountWords(path),path))