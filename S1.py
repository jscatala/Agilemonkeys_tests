#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutBamboo' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY lengths as parameter.
#

def do_ops(array):
    shortest = sorted(set(array))[0]
    return [i-shortest for i in array if i != shortest ]

def cutBamboo(lengths):
    # Write your code here
    a_lengths = []
    while len(lengths) > 0:
        a_lengths.append(len(lengths))
        lengths = do_ops(lengths)
    return a_lengths

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lengths_count = int(input().strip())

    lengths = []

    for _ in range(lengths_count):
        lengths_item = int(input().strip())
        lengths.append(lengths_item)

    result = cutBamboo(lengths)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
