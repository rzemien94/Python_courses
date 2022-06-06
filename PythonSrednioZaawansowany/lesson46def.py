# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:15:09 2022

@author: rzemi
"""

def show_progress(how_many,char="*"):
    try:
        print(how_many*char)
    except Exception as e:
        print('error',e)
        
show_progress(10)
show_progress(15)
show_progress(30)
 
show_progress(10, '-')
show_progress(15, '+')