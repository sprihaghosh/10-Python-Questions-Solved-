# -*- coding: utf-8 -*-
"""

@author: HP
"""

def frequency(arr):
    max = 0
    length = len(arr)
    
    for i in range(0,length-1):
        c = 1
        for j in range(i+1,length):
            if(arr[i]==arr[j]):
                c += 1
                if(max < c):
                    max = c
                    num = arr[i]
                    #print(i)
    print(num,"occurs with the most frequency",max)

arr1 = [2,5,4,6,4,1,2,8,2,5,6,9,6,7,6]
frequency(arr1)