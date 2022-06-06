# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:52:29 2022

@author: rzemi
"""
import random

colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

allCards=[]

for i in range(len(colors)):
    for j in range(len(figures)):
        print("the card is:",colors[i],figures[j])
        allCards.append(colors[i]+figures[j])
        
print(allCards)

random.shuffle(allCards)

print(allCards)

player1=[]
player2=[]

max=len(allCards)

for i in range(max-1):
    if i%2 == 0:
        player1.append(allCards[i])
    elif i%2 ==1:
        player2.append(allCards[i])
        
print(player1)
print(player2)