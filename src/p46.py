import time, mtools, math

def separatable(n, l):
    # n = x + 2*r*r
    for x in l:
        if x > n:
            return False
        t = n - x
        if (t%2) != 0:
            continue
        t = t/2
        r = int(math.sqrt(t))
        if r*r == t:
            return True
    return False

def solve():
    l = mtools.sieve_primes(1000000)
    l2 = list(set(range(33, 1000000, 2)) - set(l))
    for i in l2:
        if not separatable(i, l):
            return i

def test():
    l = [9, 15, 21, 25, 27, 33]
    for x in l:
        assert separatable(x, mtools.sieve_primes(100))

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
