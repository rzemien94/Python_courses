# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:44:46 2022

@author: rzemi
"""

import urllib.request
import os
 
data_dir = r'F:\Users\rzemi\Desktop\KursyPython\PythonSrednioZaawansowany'
pages = [
    { 'name': 'mobilo','url': 'http://www.mobilo24.eu/'},
    #{ 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'wikipedia', 'url': 'https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna'} ]
 
for page in pages:
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
        print("Processing: {}  => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve (page["url"], path)
        print('...done')
    except:
        print('fail for page: {}'.format(page["name"]))
        print('stop')
        break
 
else:
    print('succesfull')