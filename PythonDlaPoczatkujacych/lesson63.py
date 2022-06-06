# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:55:02 2022

@author: rzemi
"""

Tax=(4,7,8,23)
print(Tax)
print(Tax[2])
print(Tax[-1])

TaxList=list(Tax)
TaxList.append(30)
NewTax=tuple(TaxList)

print(TaxList)

print(NewTax)

(tax1,tax2,tax3,tax4)= Tax
print(tax1,tax2,tax3,tax4)

a=1
b=10

print("a = ",a,"\tb =",b)

(a,b)=(b,a)

print("a = ",a,"\tb =",b)