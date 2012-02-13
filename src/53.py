#encoding=utf-8

'''
How many values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''

import time, math, mtools

def c(n, r):
    a = mtools.fac(r)
    b = 1
    for i in range(n-r+1,n+1):
        b = b*i
    return b/a

def combs(n, max):
    r = n/2
    cnt = 0
    while c(n, r) > max:
        cnt = cnt + 2
        r = r - 1
    if (n%2 == 0):
        cnt = cnt - 1
    print cnt
    return cnt

def solve():
    sum = 0
    for i in range(23, 101):
        sum = sum + combs(i, 1000000)
    return sum

def test():
    assert c(5,2) == 10
    assert c(5,3) == 10
    assert c(23,10) == 1144066

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
