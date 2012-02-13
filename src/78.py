import math, time, mtools, sys

tab = {0:1, 1:1, 2:2}

def solve():
    i = 0
    while True:
        n = p(i)
        if (n % 1000000) == 0:
            print n, len(str(n))
            return i
        i = i + 1
        if (i % 10000 == 0):
            print i

'''
http://mathpages.com/home/kmath383.htm
One of the easiest ways of computing the sequence p(n) is recursively
using the formula

         p(n) = SUM  (-1)^(k-1)  p(n - k(3k+-1)/2)
'''
def p(n):
    global tab
    if tab.has_key(n):
        return tab[n]
    s = 0
    for k in range(1, n):
        sb = s
        i = n - k*(3*k+1)/2
        j = n - k*(3*k-1)/2
        if i >= 0:
            if k % 2 == 0:
                s = s - p(i)
            else:
                s = s + p(i)
        if j >= 0:
            if k % 2 == 0:
                s = s - p(j)
            else:
                s = s + p(j)
        if sb == s:
            tab[n] = s
            return s
    tab[n] = s
    return s


'''
test cases for p(n) are from http://www.research.att.com/~njas/sequences/b000041.txt
'''
def test():
    assert 1 == p(0)
    assert 1 == p(1)
    assert 2 == p(2)
    assert 7 == p(5)
    assert 11 == p(6)
    assert 15 == p(7)
    assert 190569292 == p(100)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
