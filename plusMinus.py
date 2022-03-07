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
    n = len(arr)
    positives = 0
    negatives = 0
    zeros = 0
    for value in arr:
        if value > 0:
            positives += 1
        elif value < 0:
            negatives += 1
        else:
            zeros += 1
    print('%.6f' %(positives/n))
    print('%.6f' %(negatives/n))
    print('%.6f' %(zeros/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)