# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:17:25 2022

@author: rzemi
"""

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i=0
maxi= len(numbers)-2

while i <= maxi:
    print(i,numbers[i])
    if numbers[i]**2 == numbers[i+1]:
        print("Find:",numbers[i],numbers[i+1])
    i+=1     
 
i=0
maxi= len(numbers)-3 

while i <= maxi:
    print(i,numbers[i])
    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
        print("Find:",numbers[i],numbers[i+1],numbers[i+2])
    i+=1
    
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i=0
imax=len(texts)-2

while i <= imax:
    print(i)
    if len(texts[i]) == len(texts[i+1]):
        print("find:",texts[i],texts[i+1])
    i+=1
                    