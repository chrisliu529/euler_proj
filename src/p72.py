import math, time, mtools, sys

def solve():
    return ns_rpf(1000000)

def test():
    assert ns_rpf(8) == 21

def ns_rpf(n):
    l = [mtools.phi(x) for x in range(2, n+1)]
    return sum(l)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
