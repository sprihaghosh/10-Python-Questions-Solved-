# -*- coding: utf-8 -*-
"""

@author: HP
"""

def double(str1):
    
    str2 = ""
    for i in str1:
       str2 = str2 + i + i
    return str2

string = str(input("Enter a string value: "))

print("The updated string is", double(string))