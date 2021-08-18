#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    j=0
    k=0
    l=0
    for i in range(0,n):
     if arr[i]==0:
        k+=1
     if arr[i]>0:
        j+=1
     if arr[i]<0:
        l+=1
    print(float(j/n),end="\n")          
    print(float(l/n), end="\n")          
    print(float(k/n))          
    
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
