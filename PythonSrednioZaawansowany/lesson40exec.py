# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:30:05 2022

@author: rzemi
"""
import os


files_to_process = [
    r"F:\Users\rzemi\Desktop\KursyPython\PythonSrednioZaawansowany\lesson40execFile1.py",
    r"F:\Users\rzemi\Desktop\KursyPython\PythonSrednioZaawansowany\lesson40execFile2.py"
    ]

for i in range(0,len(files_to_process)):
    print(os.path.basename(files_to_process[i]))
    
for file in files_to_process:
    with open(file, 'r') as f:
        source = f.read()
        exec(source)
    
