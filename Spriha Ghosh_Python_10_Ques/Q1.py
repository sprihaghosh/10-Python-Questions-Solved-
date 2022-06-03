# -*- coding: utf-8 -*-
"""

@author: HP
"""

def arrange(lst,str1):
    
    if str1 == "asc":
        asclist = sorted(lst)
        print("List in ascending order: ",asclist)
    
    elif str1 == "desc":
        desclist = sorted(lst, reverse=True)
        print("List in descending order: ",desclist)
    
    elif str1 == "none":
        print("Original list",lst)
        
    else:
        print("Invalid input")
        
list1 = []
n = int(input("\nEnter number of elements in the list: "))
   
for i in range(0,n):
        
    print("Enter the ",i,"th element:")
    ele = input()
        
    list1.append(ele)
    
str2 = str(input("Enter 'asc' or 'desc' or 'none': "))

arrange(list1,str2)