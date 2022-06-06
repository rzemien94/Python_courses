# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:50:52 2022

@author: rzemi
"""

films={
       "Finding Dory":[3,5],
       "Bourne":[18,1],
       "Ghost Busters":[12,5],
       }

while True:
    choice=input("What film would you like to watch?:").strip().title()
    if choice in films:
        try:
            age=int(input("How ald are you?:").strip())
        except:
            print("You have to press number, try again")
            continue
        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print("Enjoy the film")
                films[choice][1]-=1
            else:
                print("we have not enough places")
        else:
            print("you are too young to watch the film")
    else:
        print("We don't have that film")