#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    a = 2 * sum(set(a)) - sum(a)
    return a

if __name__ == '__main__':
    lonelyinteger([0, 0, 1, 2, 1, 2])
