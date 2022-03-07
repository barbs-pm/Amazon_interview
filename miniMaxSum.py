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
    arrMax = arr.copy()
    arr.sort()
    arrMax.sort(reverse=True)
    
    min = 0
    max = 0
    
    for i in range(4):
        min += arr[i]
        max += arrMax[i]
        
    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
