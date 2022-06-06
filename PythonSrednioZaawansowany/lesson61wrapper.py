# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:08:41 2022

@author: rzemi
"""
import functools
import time

def wrapper_time(func):
    def a_wrapped_function(*args,**kwargs):
        time_start=time.time()
        v=func(*args,**kwargs)
        time_stop=time.time()
        print(f"{func.__name__} wykonana w czasie {time_stop-time_start}")
        return v
    return a_wrapped_function

        
def get_sequence(n):    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
    
wrapper_get_sequence=wrapper_time(get_sequence)
print(wrapper_get_sequence(1)) 

@wrapper_time
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
 
print(get_sequence(1))

