# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:48:24 2022

@author: rzemi
"""

text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'

text1=text.split(' ')

print(text1)

shortText=''

for i in range(0,21):
    shortText= shortText+ text1[i]+' '

print(shortText)