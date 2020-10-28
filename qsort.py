import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    
    quickSort = arr[0]
    l = []
    r = []
    for i in range(1, len(arr)):
        if arr[i] <= quickSort:
            l.append(arr[i])
        if arr[i] > quickSort:
            r.append(arr[i])
    l.append(quickSort)
    q = l + r
    return q

if __name__ == '__main__':

    fptr = open('result.txt', 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

