# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 22:00:43 2022

@author: rzemi
"""

isAutomaticMode=False
is80PercentLight=True
isDirectLight=False
isRainy=True

turnLightsOn=(isAutomaticMode and not is80PercentLight) or (isAutomaticMode and isDirectLight) or (isAutomaticMode and isRainy)

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)