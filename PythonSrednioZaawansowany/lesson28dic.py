# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:20:29 2022

@author: rzemi
"""

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
blankList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

dict_denominations=dict(zip(banknotes_coins,blankList))

print(dict_denominations)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1
 
dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2
 
dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for coin in dict_denominations:
    print("Denominate: {0:6.2f} - amount {1:5}".format(coin, dict_denominations[coin]))