# -*- coding: utf-8 -*-
"""

@author: HP
"""

def CreditNo(number):
    
    lastfour = number[-4:]

            
    print("The credit card number is: ")       
    print("**** **** ****",lastfour)    

    
num = input("Enter your credit card number:")

if len(num) != 16:        
  print("Invalid input, try again ")
        
else:
    CreditNo(num)
