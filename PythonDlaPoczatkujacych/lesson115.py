# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:30:03 2022

@author: rzemi
"""
import math

degree=360

print("dla",degree," stopni jest:",degree*math.pi/180,"radianów")
print("z funkcji:",math.radians(degree))

small=0.22
priceS=11.5
big=0.27
priceB=15.6
familly=0.38
priceF=22

print("pole small:",math.pi*math.pow(small, 2))
print("pole big:",math.pi*math.pow(big, 2))
print("pole familly:",math.pi*math.pow(familly, 2))

print("proce for m^2 small:",priceS/(math.pi*math.pow(small, 2)))
print("proce for m^2 big:",priceB/(math.pi*math.pow(big, 2)))
print("proce for m^2 familly:",priceF/(math.pi*math.pow(familly, 2)))


