#encoding=utf-8
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, 
find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

import time

def d(n):
    return 9*n*(10**(n-1))

def s(n):
    i = 1
    t = d(i)
    while n > t:
        n = n - t
        i = i + 1
        t = d(i)

    return p(n, i)

def p(n, i):
    if i > 1:
        r = 10**(i-1) + n/i
    else:
        r = n/i
    ds = separate_digits(r)
    return ds[(n-1)%i]

def separate_digits(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n / 10
    l.reverse()
    return l

def test():
    assert d(1) == 9
    assert separate_digits(10) == [1,0]
    assert separate_digits(123) == [1,2,3]
    assert s(1) == 1
    assert s(10) == 1
    assert s(11) == 1
    assert mul([1,2,3]) == 6

def mul(l):
    m = 1
    for x in l:
        m = m * x
    return m

def solve():
    l = [s(10**x) for x in range(0, 7)]
    return mul(l)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
