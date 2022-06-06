# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 08:34:01 2022

@author: rzemi
"""
import sys
import os

file_path = r'F:\Users\rzemi\Desktop\KursyPython\PythonDlaPoczatkujacych\Testowe\data_input\orders.csv'
 
with open(file_path,"r") as file:
 
    for line in file:
        try:
            line = line.replace('\n','')
            order = line.split(',')
     
            pharmacy_name=order[0]
            item=order[1]
            amount=int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' % (pharmacy_name,item,amount))
        except ValueError as e:
            print("incorrect conversion:",e,"in line:",line)
        except IndexError as e:
            print("lack of information:",e,"in line:",line)
        except:
            print("Error:", sys.exc_info()[0])
print("Processing finished")