# -*- coding: utf-8 -*-
"""

@author: HP
"""

import random
arr1 = []
for i in range(1,99):
    arr1.append(i)
    
a = random.randint(1,100)
arr1.append(a)

print(arr1)

length = len(arr1)

for i in range(length):
    x = arr1[i] % length
    #print(x)
    arr1[x] += length
    #print(arr1[x])
    
for j in range(length):
    #print(arr1[j])
    if (arr1[j] >= length*2):
        print("The duplicated element is",j)