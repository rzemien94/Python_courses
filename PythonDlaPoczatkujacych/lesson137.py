# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:13:22 2022

@author: rzemi
"""

width=20
height=5
numbers=[1]
line=''
for n in numbers:
    line+="%3d" % (n)
print(line.center(width))

for i in range(height-1):
    newNumbers=[1]
    position=0
    while position < len(numbers) -1:
        newNumbers.append(numbers[position]+numbers[position+1])
        position+=1
    newNumbers.append(1)
    numbers=newNumbers.copy()
    line=''
    for n in numbers:
        line+="%3d" % (n)
    print(line.center(width))
