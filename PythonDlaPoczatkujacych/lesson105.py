# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:46:13 2022

@author: rzemi
"""

initialCapital=20000
percent=0.03
maxTimeYears=10
actualTime=0
actualCapital=initialCapital

while actualTime < maxTimeYears:
    actualCapital=round(actualCapital*(percent+1),2)
    actualTime+=1
    print("You have earn:", actualCapital-initialCapital,"For:",actualTime, "Years")
    

number = 20730906
numberStr= str(number)
numberLength= len(numberStr)
i=0
sum=0

while i < numberLength:
    sum=sum+int(numberStr[i])
    i+=1
print("the sum is:",sum)

text='''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''

textSplit=text.replace('\n',' ').split(' ')
length=len(textSplit)
i=0
j=0
k=0
wordLength = 6

while i < length:
    if len(textSplit[i]) > wordLength:
        j+=1
    else:
        k+=1
    i+=1
print("The words longer than",wordLength,"in that text is:",j,"shorter:",k)

    