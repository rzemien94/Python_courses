# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:27:42 2022

@author: rzemi
"""

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']

sumOfPoints = 4988

min=100
max=0
percentLength=len(percent)
i=0

while i < percentLength:
    if float(percent[i]) < min:
        min=float(percent[i])
    elif float(percent[i]) > min:
        max=float(percent[i])
    i+=1

print ("Min percent:",min,"Max percent:",max)

for i in range (len(countries)):
    print(percent[i],int(percent[i]),round(float(percent[i]),2),float(percent[i])*sumOfPoints/100,countries[i])
        