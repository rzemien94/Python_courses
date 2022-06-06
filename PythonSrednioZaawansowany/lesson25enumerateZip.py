# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:03:35 2022

@author: rzemi
"""

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for project,author in zip(projects,leaders):
    print('The leader of ',project,'is ',author)
    
    
    
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
for pos,(project,(date,author)) in enumerate(zip(projects,zip(dates,leaders))):
    print(pos,'- The leader of ',project,'started ',date,'is ',author)