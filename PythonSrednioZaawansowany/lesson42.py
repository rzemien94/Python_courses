# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:35:48 2022

@author: rzemi
"""
import time


source="reportLine+=1"

reportLine=0
start=time.time()
for i in range(100000):
    exec(source)
stop=time.time()
timeNotCompiled=stop-start

start=time.time()
sourceCompiled=compile(source,'internal variable source','exec')
for i in range(100000):
    exec(sourceCompiled)
stop=time.time()
timeCompiled=stop-start

print(timeNotCompiled,timeCompiled,timeNotCompiled/timeCompiled)