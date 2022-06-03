# -*- coding: utf-8 -*-
"""

@author: HP
"""

def addintegers(str1):
    summ = 0
    for i in str1:
        if i.isdigit() == True:
            j = int(i)
            summ += j
    print("The sum of all the integers in the string ",str1, " are ",summ)
    
string = str(input("Enter a string: "))
addintegers(string)