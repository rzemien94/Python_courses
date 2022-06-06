# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:45:23 2022

@author: rzemi
"""

import math,time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)
    
for formula in formulas_list:
    results_list=[]
    print(formula)
    start=time.time()
    for arg in range(len(argument_list)):
        x=argument_list[arg]
        output=eval(formula)
        results_list.append(output)
    print(min(results_list))
    print(max(results_list))
    stop=time.time()
    print('time of counting: ',stop-start)
    
    
for formula in formulas_list:
    results_list=[]
    print(formula)
    start=time.time()
    compiled_formula=compile(formula,'internal variable source','eval')
    for arg in range(len(argument_list)):
        x=argument_list[arg]
        output=eval(compiled_formula)
        results_list.append(output)
    print(min(results_list))
    print(max(results_list))
    stop=time.time()
    print('time of counting: ',stop-start)