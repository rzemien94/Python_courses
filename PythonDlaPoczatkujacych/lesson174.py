# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:50:25 2022

@author: rzemi
"""

file_path="F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\data_input\\orders.csv"
with open(file_path,"r") as file:
    for line in file:
        line=line.replace("\n", "")
        line=line.split(",")
        if len(line) == 3:
            print("Order from drugstore %s, item %s, amount %s" % (line[0],line[1],line[2]))
        else:
            print("Line %s malformed!!!" % (line))