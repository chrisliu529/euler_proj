import math, time, mtools, sys

def solve():
    n = 428571
    d = 0
    while True:
        if (7*n+1) % 3 == 0:
            d = (7*n+1) / 3
            print '(n,d) = (%s,%s)' % (n, d)
            break
        n = n - 1
    l1 = mtools.prime_factors(n)
    l2 = mtools.prime_factors(d)
    print l1,l2
    return 'n in hcf(n,d)'

def test():
    pass

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
