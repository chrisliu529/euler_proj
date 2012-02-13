import math, time, mtools, sys

def solve():
    max_r = 0
    max_n = 0
    for n in range(2, 1000001):
        p = phi(n)
        r = float(n)/p
        if r > max_r:
            max_r = r
            max_n = n
    return max_n

def test():
    assert phi(2) == 1
    assert phi(7) == 6
    assert phi(10) == 4
    assert phi(12) == 4
    assert phi(30) == 8
    assert mul([1,2,3]) == 6

def phi(n):
    p, c = mtools.prime_factors(n)
    s = n
    for x in p:
        s = s - s/x
    return s

def mul(l):
    m = 1
    for x in l:
        m = m*x
    return m

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
