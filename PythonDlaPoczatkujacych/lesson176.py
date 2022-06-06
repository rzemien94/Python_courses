# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:58:05 2022

@author: rzemi
"""

filename="F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\test.txt"
line="Europe"
cities=["a","b","c"]

file=open(filename,"a")
file.write(line)
file.writelines("\n")
#file.writelines(cities)
for city in cities:
    file.write(city+"\n")
file.close()