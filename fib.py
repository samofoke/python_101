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
