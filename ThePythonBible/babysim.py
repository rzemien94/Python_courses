# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:42:57 2022

@author: rzemi
"""
import random
questions=["Why is the sky blue","Why is there a face on the moon?","Where are all the dinosaurs?"]

answer=input(random.choice(questions)).lower()

while answer != "just because":
    answer=input("Why?:").strip().lower()
    
print("Oh...  ok")