# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:35:27 2022

@author: rzemi
"""
'''
file=open("F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\test.txt","r")

content=file.read()

#print(content)


file.close()

with open("F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\test.txt","r") as file:
    content=file.read()
    #print(content)
    
with open("F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\test.txt","r") as file:
    for line in file:
        #print(line)
 '''     
file=open("F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\test.txt","r")
fragment=file.read(10)
while fragment:
    print(fragment)
    fragment=file.read(10)
file.close()