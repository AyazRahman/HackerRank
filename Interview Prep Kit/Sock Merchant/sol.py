#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    pairs = {}
    
    for i in ar:
        if i in pairs:
            pairs[i]+=1
        else:
            pairs[i]=1

    result = 0
    for i in pairs.values():
        result+=i/2
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
