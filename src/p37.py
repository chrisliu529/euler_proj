'''
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import time, mtools

def is_truncatable(n):
    return left_trunkable(n) and right_trunkable(n)

def right_trunkable(n):
    while n > 10:
        n = n / 10
        if not mtools.is_prime(n):
            return False
    return True

def left_trunkable(n):
    p = len(str(n))
    d = 10**(p - 1)
    while n > 10:
        n = n % d
        if not mtools.is_prime(n):
            return False
        d = d / 10
    return True

def solve():
    l = mtools.sieve_primes(1000000)
    l = [x for x in l if x > 10 and is_truncatable(x)]
    print l
    assert len(l) == 11
    return sum(l)

def test():
    assert is_truncatable(3797)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
