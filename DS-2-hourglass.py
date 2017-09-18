#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
min_sum=-1000
for i in range(0,len(arr)-2):
    for j in range(0,len(arr[i])-2):
        s=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        min_sum=max(s,min_sum)
print(min_sum)
