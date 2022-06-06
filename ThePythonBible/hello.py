# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:42:47 2022

@author: rzemi
"""

name=input("your name is:")

age=input("your age is:")


while True:
    if age.isdecimal():
        break;
    else:
        print("try again, your age must be  a number:cos")
        age=input("your age is:")

city=input("your city is:")

hobby=input("your hobby is:")

string= print("info about you are: \nname - %s\nage -%s\ncity - %s\nhobby - %s\n" % (name,age,city,hobby))

string2="Your name is {} and you are {} years old. You live in {} and you love {}"
output=string2.format(name,age,city,hobby)

print(output)

