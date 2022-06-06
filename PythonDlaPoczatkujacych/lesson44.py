# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:18:52 2022

@author: rzemi
"""

helloMessage="Hello %s!"
print(helloMessage % ('kate'))
print(helloMessage % ('chris'))

helloMessage="Hello {0:s}!"
print(helloMessage.format('kate'))
print(helloMessage.format('chris'))

helloMessage="%s has %d %s"
print(helloMessage % ('kate',1,'animal'))
print(helloMessage % ('chris',100000,'$'))

helloMessage="{0:s} has {1:d} {2:s}"
print(helloMessage.format('kate',1,'animal'))
print(helloMessage.format('chris',100000,'$'))

line='%20s costs %6d €' 
print(line % ('ice cream',3))
print(line % ('trip to venice',119))
print(line % ('pizza hawai',6))