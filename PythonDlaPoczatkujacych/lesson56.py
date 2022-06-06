# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:25:12 2022

@author: rzemi
"""

q="THE EYES"
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])

line='Program "Kropka nad i" nadamy o: 22:oo'

time=line[line.find(':')+2:]
print(time)

tmp= line[line.find('"')+1:]
print(tmp)

title=tmp[:tmp.find('"')]
print(title)

line='Program "Pytanie na śniadanie" nadamy o: 6:00'

time=line[line.find(':')+2:]
print(time)

tmp= line[line.find('"')+1:]
print(tmp)

title=tmp[:tmp.find('"')]
print(title)


