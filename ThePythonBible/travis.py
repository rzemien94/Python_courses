# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:22:27 2022

@author: rzemi
"""

knownUsers=["Anna","Bob","CLaire","Dan","Emma","Fred","George","Harry"]

print(len(knownUsers))

while True:
    print("Hi, my name is Travis")
    name=input("what is your name?").strip().capitalize()
    if name in knownUsers:
        print("name recognised")
        print("Hello {}!".format(name))
        remove=input("Would you like to be removed from the system (y/n)?:").lower()
        if remove == "y":
            knownUsers.remove(name)
        elif remove == "n":
            print("ok, you are still on the system")
            
    else:
        print("Hmmm I dont't think I have met you yet {}".format(name))
        add=input("Would you like to be add to the system (y/n)?:").lower()
        if add == "y":
            knownUsers.append(name)
        elif add == "n":
            print("ok, you are not on the system")