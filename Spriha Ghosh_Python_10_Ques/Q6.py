# -*- coding: utf-8 -*-
"""

@author: HP
"""

lower = int(input("Enter the starting value of the range: "))
upper = int(input("Enter the ending value of the range: "))

ind = 0

print("The prime numbers between ",lower," and ",upper," are:")

for i in range(lower, upper+1):
    
    if i==1:
        continue
    ind = 1
    
    for j in range(2, i//2 + 1): #to check divisibility of i with all the numbers present before
        if i%j == 0:
            ind = 0
            break
        
    if ind == 1: #indicates a prime number
        print(i)