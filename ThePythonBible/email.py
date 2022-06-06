# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 20:28:42 2022

@author: rzemi
"""

email=input("press email address:").strip()

user=email[:email.index("@")]

domain=email[email.index("@")+1:]

output="username is {} and domain is {}"

output=output.format(user, domain)

print(output)