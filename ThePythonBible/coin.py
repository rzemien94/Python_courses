# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:39:43 2022

@author: rzemi
"""
import random

class Coin:
    def __init__(self,rare=False,clean=True,heads=True,**kwargs):
        
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.isRare=rare
        self.isClean=clean
        self.heads=heads
        
        if self.isRare:
            self.value=self.originalValue*1.25
        else:
            self.value=self.originalValue
            
        if self.isClean:
            self.colour=self.cleanColour
        else:
            self.colour=self.rustyColour
            
    def rust(self):
        self.colour=self.rustyColour
        
    def clean(self):
        self.colour=self.cleanColour
        
    def __del__(self):
        print("Coin Spent!")
        
    def flip(self):
        headsOptions=[True,False]
        choice=random.choice(headsOptions)
        self.heads=choice()
        
    def __str__(self):
        if self.originalValue >= 1:
            return "£{} Coin".format(int(self.originalValue))
        else:
            return "{}p Coin".format(int(self.originalValue * 100))
        
        

class OnePound(Coin):
    def __init__(self):
        data={
            "originalValue":1.00,
            "cleanColour":"gold",
            "rustyColour":"greenish",
            "numEdges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5
            }
        super().__init__(**data)
        
class TwoPound(Coin):
    def __init__(self):
        data={
            "originalValue":2.00,
            "cleanColour":"gold & silver",
            "rustyColour":"greenish",
            "numEdges":1,
            "diameter":28.4,
            "thickness":2.50,
            "mass":12.00
            }
        super().__init__(**data)
        
class OnePence(Coin):
    def __init__(self):
        data={
            "originalValue":0.01,
            "cleanColour":"bronze",
            "rustyColour":"brownish",
            "numEdges":1,
            "diameter":20.3,
            "thickness":1.52,
            "mass":3.56
            }
        super().__init__(**data)

class TwoPence(Coin):
    def __init__(self):
        data={
            "originalValue":0.02,
            "cleanColour":"bronze",
            "rustyColour":"brownish",
            "numEdges":1,
            "diameter":25.9,
            "thickness":1.85,
            "mass":7.12
            }
        super().__init__(**data)
    
class FivePence(Coin):
    def __init__(self):
        data={
            "originalValue":0.05,
            "cleanColour":"silver",
            "rustyColour":None,
            "numEdges":1,
            "diameter":18.0,
            "thickness":1.77,
            "mass":3.25
            }
        super().__init__(**data)
        
    def rust(self):
        self.colour=self.cleanColour
        
    def clean(self):
        self.colour=self.cleanColour
        
class TenPence(Coin):
    def __init__(self):
        data={
            "originalValue":0.10,
            "cleanColour":"silver",
            "rustyColour":None,
            "numEdges":1,
            "diameter":24.5,
            "thickness":1.85,
            "mass":6.50
            }
        super().__init__(**data)
        
    def rust(self):
        self.colour=self.cleanColour
        
    def clean(self):
        self.colour=self.cleanColour
        
class TwentyPence(Coin):
    def __init__(self):
        data={
            "originalValue":0.20,
            "cleanColour":"silver",
            "rustyColour":None,
            "numEdges":7,
            "diameter":21.4,
            "thickness":1.7,
            "mass":5.00
            }
        super().__init__(**data)
        
    def rust(self):
        self.colour=self.cleanColour
        
    def clean(self):
        self.colour=self.cleanColour
        
class FiftyPence(Coin):
    def __init__(self):
        data={
            "originalValue":0.50,
            "cleanColour":"silver",
            "rustyColour":None,
            "numEdges":7,
            "diameter":27.3,
            "thickness":1.78,
            "mass":8.00
            }
        super().__init__(**data)
        
    def rust(self):
        self.colour=self.cleanColour
        
    def clean(self):
        self.colour=self.cleanColour
        
coins=[OnePence(),TwoPence(),FivePence(),TenPence(),TwentyPence(),FiftyPence(),OnePound(),TwoPound()]

for coin in coins:
    arguments=[coin,coin.colour,coin.value,coin.diameter,coin.thickness,coin.numEdges,coin.mass]
    string = "{} - Colour: {}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    print(string)