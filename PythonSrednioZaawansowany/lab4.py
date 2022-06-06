# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:53:02 2022

@author: rzemi
"""

a=b=c=10
print(a,b,c,id(a),id(b),id(c))
a=20
print(a,b,c,id(a),id(b),id(c))

a=b=c=[1,2,3]
print(a,b,c,id(a),id(b),id(c))
a.append(4)
print(a,b,c,id(a),id(b),id(c))

x=10
y=10
print(x,y,id(x),id(y))

y=y+1-1
print(x,y,id(x),id(y))

y=y+1234567890
y=y-1234567890
print(x,y,id(x),id(y))