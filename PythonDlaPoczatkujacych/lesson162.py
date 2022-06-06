# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:23:30 2022

@author: rzemi
"""

import math

def GiveGeomSeqElement(a1=2,factor=2,index=2):
    #oblcizenia na ciagach geometrycznych
    an=a1*math.pow(factor, index-1)
    
    return an

for i in range(1,10):
    print(GiveGeomSeqElement(3,2,i))
    
def GiveFactorForGeomSeq(term,nexterm):
    #find out actual factor
    value=nexterm/term
    return value

print(GiveFactorForGeomSeq(12, 24))

def GiveSumOfNElementsGeomSeq(a1=2,factor=2,n=2):
    sum=(a1*(1-math.pow(factor, n)))/(1-factor)
    return sum

print(GiveSumOfNElementsGeomSeq(2,3,4))

