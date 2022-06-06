# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:03:44 2022

@author: rzemi
"""

import os

webaddresses=[]

line=input("www adress:")

while len(line) != 0:
    webaddresses.append(line)
    print("if you wat to finisch press enter witout any text")
    line=input("www adress:")
    
dirname=os.getcwd()

filename=input("give filename:")
filepath=os.path.join(dirname, filename)

file=open(filepath,"a")
for wa in webaddresses:
    file.write(wa+"\n")
file.close()
#---------------------------------------
filename=filepath
while True:
    if os.path.isfile(filename):
        break
    else:
        filename=input("filepath:")

webaddresses=[]
with open(filename,"r") as file:
    for line in file:
        line=line.replace("\n", "")
        line=webaddresses.append(line)

for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')
#----------------------------------------
        
filename=filepath
while True:
    if os.path.isfile(filename):
        break
    else:
        filename=input("filepath:")

webaddresses=[]
with open(filename,"r") as file:
    for line in file:
        line=line.replace("\n", "")
        line=webaddresses.append(line)
filePLpath="F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\PLadress.txt"
filenotPLpath="F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\notPLadress.txt"


for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
        with open(filePLpath,"a") as file1:
            file1.write(line+"\n")
    else:
        print(line, 'is not a polish web page')
        with open(filenotPLpath,"a") as file2:
            file2.write(line+"\n")