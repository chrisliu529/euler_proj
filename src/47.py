import time, mtools, math

def solve():
    for i in range(1000, 1000000):
        if primes_n(i, 4):
            return i

def primes_n(s, n):
    for i in range(s, s+n):
        p, num = mtools.prime_factors(i)
        if len(p) != n:
            return False
    return True

def test():
    assert primes_n(14, 2)
    assert primes_n(644, 3)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
