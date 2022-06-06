# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:20:24 2022

@author: rzemi
"""

def DoAction(action,parameter):
    print(action)
    print(parameter)
    return

DoAction('buy', 'shoes')

def DoAction1(action,*parameter):
    print(action)
    print(parameter)
    for element in parameter:
        print("for",element)
    return

DoAction1('buy', 'shoes', 'socks')

def DoAction2(action, what,**parameter):
    print(action)
    print(what)
    print(parameter)
    for element in parameter:
        print("for",parameter[element])
    return

DoAction2('buy', 'shoes', size=45,color='brown')