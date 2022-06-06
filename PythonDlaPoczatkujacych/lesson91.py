# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:58:00 2022

@author: rzemi
"""
datas = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
elements=[]
for data in datas:
    print(data.upper())
    elements=data.split(':')
    print(elements[0].upper())
    print(elements[1])
