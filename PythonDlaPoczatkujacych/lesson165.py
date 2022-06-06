# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:00:42 2022

@author: rzemi
"""
import math

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

print("rownanie kwadratowe: y=ax^2+bx+c")
while True:
    a=input("podaj a:")
    if check_int(a):
        a=int(a)
        break
    else:
        print("the parameter a has to be a decimal")
while True:
    b=input("podaj b:")
    if check_int(b):
        b=int(b)
        break
    else:
        print("the parameter b has to be a decimal")
while True:
    c=input("podaj c:")
    if check_int(c):
        c=int(c)
        break
    else:
        print("the parameter c has to be a decimal")
if a != 0:
    delta=math.pow(b, 2)-(4*a*c)
    
    if delta > 0:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("the result is %f and %f" % (x1,x2))
    elif delta == 0:
        x1=(-b-math.sqrt(delta))/(2*a)
        print("the result is %f" % (x1))
    else:
        print("delta is less than 0, the program was stopped.")
else:
    print("this is not a valid data for a")
