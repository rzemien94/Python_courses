# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:47:46 2022

@author: rzemi
"""

article='''"Pythonesque" redirects here. For the play by Roy Smiles, see Pythonesque (play).
"The Pythons" redirects here. For the documentary film about the group, see The Pythons (film).
This article is about the comedy group. For their TV show frequently called Monty Python, see Monty Python's Flying Circus.'''

print(article.upper())

print(article.replace('monthy', 'python'))

print('word python appears',article.lower().count('python'),'times')

print('to print the \\ you need to put \\ twice in your text like this: \\\\ ')

print('The best hits of \'80s!!! ')
print("The best hits of '80s!!!") 

amountPLN= 234
print('cur\t\texchange\tamount')
print('USD','\t\t',3.65,'\t\t',amountPLN/3.65)
print('EUR','\t\t',4.23,'\t\t',amountPLN/4.23)

valueAsText='123.45'
factor=1.23

print('value is',valueAsText, 'factor is', str(factor), 'value*factor=', float(valueAsText)*factor )