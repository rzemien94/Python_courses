# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:27:27 2022

@author: rzemi
"""

product=[0,1,2,3,4,5]
listA=product.copy()
listB=product.copy()
'''
for a in listA:
    for b in listB:
        product.append((a,b))
print(product)

producent=[(a,b) for a in listA for b in listB]
print(product)

producent=[(a,b) for a in listA for b in listB if a % 2 == 1 and b %w == 0]
print(product)

producent={a:b for a in listA for b in listB if a % 2 == 1 and b %w == 0}
print(product)
'''
gen=((a,b) for a in listA for b in listB if a % 2 == 1 and b %2 == 0)
print(gen)

print(next(gen))
print(next(gen))
print('-'*30)
for x in gen:
    print(x)
print('-'*30)
for x in gen:
    print(x)
    
gen=((a,b) for a in listA for b in listB if a % 2 == 1 and b %2 == 0)
print(gen)
print('*'*30)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print('stop of generator')
        break
    