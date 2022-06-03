# -*- coding: utf-8 -*-
"""

@author: HP
"""

def calculate(x,operator,y):
    
    if operator == "+":
        res1 = x+y
        print(x,"+",y,"=",res1)
    
    elif operator == "-":
        res2 = x-y
        print(x,"-",y,"=",res2)
        
    elif operator == "/":
        res3 = x/y
        print(x,"/",y,"=",res3)
        
    elif operator == ".":
        res4 = x*y
        print(x,".",y,"=",res4)
        
int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))

op = str(input("Mathematical operation to apply?(+,-,/,.)  "))

calculate(int1,op,int2)