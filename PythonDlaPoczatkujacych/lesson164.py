# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 10:44:44 2022

@author: rzemi
"""

#filename=input("enter filename:")

#print("the filename is: %s" % (filename))

while True:
    filesizeStr=input("enter the max file size (MB):")
    if filesizeStr.isdecimal():
        filesizeInt=int(filesizeStr)
        break
           
print("the max size in KB is: %s" % (filesizeInt*1024))