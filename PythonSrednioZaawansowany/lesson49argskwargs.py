# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:35:19 2022

@author: rzemi
"""

def calculate_paint(efficency_ltr_per_m2,*mkw,):
    try:
        x=0
        for i in range(len(mkw)):
            x+=efficency_ltr_per_m2*mkw[i]
        print(mkw)
        print(x)
    except Exception as e:
        print(e)
        
calculate_paint(2, 10,20,30)
lista=[100,200,300]
calculate_paint(2, *lista)

def log_it(*args,path='F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonSrednioZaawansowany\\log.txt'):
    with open(path,'a') as f:
        for i in range(len(args)):
            print(args[i],file=f,end=" ")
        print("\n",file=f)
    f.close()
        
log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')