# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:55:31 2022

@author: rzemi
"""

org=input("Sentnce:").strip().lower()

words=org.split(" ")

nWords=[]

for word in words:
    if word[0] in "aeiou":
        nWord=word+"yay"
        nWords.append(nWord)
    else:
        vovelPos=0
        for letter in word:
            if letter not in "aeiou":
                vovelPos=vovelPos+1
            else:
                break
        cons=word[:vovelPos]
        theRest=word[vovelPos:]
        nWord=theRest+cons+"ay"
        nWords.append(nWord)

output=" ".join(nWords)  

print(output)    