import random
import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

ops = [add, sub]
ops_str = '+-'

lim = int(sys.argv[1])

while True:
    c = random.randint(1, lim)
    if c == 1:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        r = ops[c-1](a, b)
        if r <= 5:
            continue
        print '\n%s + %s' % (a, b)
    else:
        a = random.randint(1, 19)
        b = random.randint(1, 19)
        r = ops[c-1](a, b)
        if r < 0:
            continue
        print '\n%s - %s' % (a, b)
    raw_input()
    print '\b%s %s %s = %s' % (a, ops_str[c-1], b, r)
