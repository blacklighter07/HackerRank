#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    jam = arr.copy()
    arr.sort()
    jam.sort()
    arr.pop()
    k=sum(arr)
    jam.pop(0)
    j=sum(jam)
    print(k,j)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
