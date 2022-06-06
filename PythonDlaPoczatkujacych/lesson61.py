# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:45:17 2022

@author: rzemi
"""

hitsTitle=['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitle.append('CHILD IN TIME')
hitsTitle.append('AGAIN')

hitsTitle.insert(2, 'HOTEL CALIFORNIA')
hitsTitle.insert(0, 'THE SOUND OF SILENCE')

print(hitsTitle)

print(hitsTitle.index('HOTEL CALIFORNIA'))

hitsTitle.remove('HOTEL CALIFORNIA')

hitsTitle[0]="ENJOY THE SILENCE"

print(hitsTitle)

hitsToRide= hitsTitle.copy()

hitsToRide.reverse()

print(hitsToRide)

hitsToRide.sort()
print(hitsToRide)

hitsToRide.pop(0)
hitsToRide.pop(0)
print(hitsToRide)

additionalSongs=['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
hitsToRide.extend(additionalSongs)
print(hitsToRide)
