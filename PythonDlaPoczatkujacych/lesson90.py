# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:47:08 2022

@author: rzemi
"""

persons=['El','St','Se','Ma','Sv','Ra']

domain='mycompany.com'

for person in persons:
    email=person +'@'+domain
    print(email)
else:
    print("end of th list")