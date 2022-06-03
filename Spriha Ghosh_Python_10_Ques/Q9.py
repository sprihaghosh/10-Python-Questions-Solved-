# -*- coding: utf-8 -*-
"""

@author: HP
"""

def sortStr(str1):
    newstr = sorted(str1)
    for i in newstr:
        print(i, end = " ")
    
str2 = str(input("Enter a string to sort its characters: "))

print("The characters of the string ",str2," in ascending order is:")
sortStr(str2)