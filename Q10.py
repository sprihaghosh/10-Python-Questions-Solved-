# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 14:15:06 2022

@author: HP
"""

a = 46
b = 6
print("Value of a before swapping: ",  a)
print("Value of b before swapping: ",  b)

a = a ^ b
b = a ^ b

a = a ^ b 

print("Value of a after swapping: ",  a)
print("Value of b after swapping: ",  b)