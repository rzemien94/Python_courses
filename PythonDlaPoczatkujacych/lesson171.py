# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:25:07 2022

@author: rzemi
"""

import os
import datetime

data_input_catalog="F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\data_input"
print(data_input_catalog)

data_output_catalog="F:\\Users\\rzemi\\Desktop\\KursyPython\\PythonDlaPoczatkujacych\\Testowe\\data_output"
print(data_output_catalog)

today=datetime.datetime.today()

today_output_catalog=os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
print(today_output_catalog)

is_input_catalog_ok= os.path.exists(data_input_catalog)
is_output_catalog_ok= os.path.exists(data_output_catalog)
is_today_output_catalog_ok=not os.path.exists(today_output_catalog)

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print("Conditions met! We can continue!")
elif not is_input_catalog_ok:
    print("lack od input catalog")
elif not is_output_catalog_ok:
    print("lack od output catalog")
elif not today_output_catalog:
    print("Today catalog already exist")