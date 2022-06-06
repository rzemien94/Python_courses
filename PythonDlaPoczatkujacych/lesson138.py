# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:27:43 2022

@author: rzemi
"""

import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards=[]

for i in colors:
    for j in figures:
        aCard=j.copy()
        aCard['Color']=i
        allCards.append(aCard)

random.shuffle(allCards)

#print(allCards)

player1=[]
player2=[]
max=len(allCards)

for i in range(max-1):
    if i%2 == 0:
        player1.append(allCards[i])
    elif i%2 ==1:
        player2.append(allCards[i])


while len(player1) > 0 and len(player2) > 0:
    stock=[]
    card1=player1.pop(0)
    card2=player2.pop(0)
    if card1['Power'] == card2['Power']:
        print('THE WAR')
        while card1['Power'] == card2['Power']:
            stock.append(card1)
            stock.append(card2)
            if len(player1) < 2:
                player2.append(stock)
                player2.append(player1)
                player1.clear()
                break;
            elif len(player2) < 2:
                player1.append(stock)
                player1.append(player2)
                player2.clear()
                break;
            else:
                card1=player1.pop(0)
                card2=player2.pop(0)
                stock.append(card1)
                stock.append(card2)
                card1=player1.pop(0)
                card2=player2.pop(0)
    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card1)
        player2.append(card2)
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')

if len(player1) == 0:
    print("winner is player2")
else:
     print("winner is player1")       
        
        

