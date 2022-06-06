# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 19:49:50 2022

@author: rzemi
"""

class Account:
    def __init__(self, name, balance, minBalance):
        self.name=name
        self.balance=balance
        self.minBalance=minBalance
        
    def deposit(self,amount):
        self.balance+= amount
        
        
    def withdraw(self,amount):
        if self.balance-amount >=self.minBalance:
            self.balance-=amount
        else:
            print("sorry!not enough funds")
            
    def statement(self):
        print("AccountBalance: {}".format(self.balance))


class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,minBalance=-1000)
    
    def __str__(self):
        return "{}'s Current Account: Balance {}".format(self.name, self.balance)
        
class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,minBalance=0)
        
    def __str__(self):
        return "{}'s Savings Account: Balance {}".format(self.name, self.balance)

        