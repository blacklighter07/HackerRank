#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import operator

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    # arr.sort()
#    freq = Counter(arr)
#    return (max(freq, key=freq.get))
    count = [0]*6
    for t in arr:
        count[t] += 1
    return (count.index(max(count)))
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
