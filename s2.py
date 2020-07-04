#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxProfit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER costPerCut
#  2. INTEGER salePrice
#  3. INTEGER_ARRAY lengths

def profit(pieces, length, cuts):
    """
    profit function:
    in:
       prieces: number of pieces
       lenght: lenght of rod
       cuts: cuts made to the rod
    out: 
       prifit generated
    """
    adds = pieces*length*salePrice
    cost = cuts*costPerCut
    return adds - cost

def get_max(pos, curr_max_length):
    """
    function that calculate if we can cut the rod in lenghts[pos] in size curr_max_lenght
    if we cannot cut it, then return 0, else return the profit for current lenght 
    """
    if curr_max_length <= lengths[pos]:
        mod = lengths[pos] // curr_max_length
        does_fit = (lengths[pos] % curr_max_length) == 0
        cuts = mod
        if does_fit:
            cuts -= 1
        return profit(mod, curr_max_length, cuts) 
    else:
        return 0


def maxProfit(costPerCut, salePrice, lengths):
    # Write your code here
    #Get the biggest rod. Max cut length = lenght longest rod
    max_length = max(lengths)

    #table[i][j] that will store our profits
    #i: number of rods + base case 0
    #j: lenght size from 0 to max_lenght 
    table = [[0]*(max_length+1) for i in range(len(lengths)+1)]

    #max_price: our max. profit value
    max_price = -1
    for i in range(1,len(lengths)+1):
        for j in range(1,max_length+1):
            table_w = get_max(i-1,j) + table[i-1][j]
            table_wo = table[i-1][j]
            table[i][j] = max(table_w, table_wo)
            if max_price < table[i][j]:
                max_price = table[i][j]
    
    return max_price

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    costPerCut = int(input().strip())

    salePrice = int(input().strip())

    lengths_count = int(input().strip())

    lengths = []

    for _ in range(lengths_count):
        lengths_item = int(input().strip())
        lengths.append(lengths_item)

    result = maxProfit(costPerCut, salePrice, lengths)

    fptr.write(str(result) + '\n')

    fptr.close()
