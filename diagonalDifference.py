#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sumLR, sumRL = 0,0
    for i in range(len(arr)):
        sumLR += arr[i][i]
        sumRL += arr[i][-i-1]
    return abs(sumLR-sumRL)

if __name__ == '__main__':
    print(diagonalDifference(([11, 2, 4],[4,5,6],[10,8,-12])))
