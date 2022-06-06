# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:36:13 2022

@author: rzemi
"""

colors=["red", "orange", "green", "violet", "blue", "yellow"]

cat3=colors[:3]

cat5=colors.copy()

print(cat3,cat5)

def GiveColors(list,n):
    list2=list[:n]
    return list2

print(GiveColors(["red", "orange", "green", "violet", "blue", "yellow"], 3))

for i in range(1,len(colors)):
    print(GiveColors(colors, i))
    
tekst='''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'''

tekst=tekst.split(" ")
tekst=tekst[1:12]
tekst=' '.join([str(element) for element in tekst])
print(tekst)

print(tekst[tekst.index('(')+1:tekst.index(')')])
    
    
    
    