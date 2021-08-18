#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    freq = [0] * k
     
    # Count occurrences of all remainders
    for i in range(n):
        freq[ar[i] % k]+= 1
         
    # If both pairs are divisible by 'K'
    sum = freq[0] * (freq[0] - 1) / 2;
     
    # count for all i and (k-i)
    # freq pairs
    i = 1
    while(i <= k//2 and i != (k - i) ):
        sum += freq[i] * freq[k-i]
        i+= 1
 
    # If K is even
    if( k % 2 == 0 ):
        sum += (freq[k//2] * (freq[k//2]-1)/2);
    
    return int(sum)    

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
