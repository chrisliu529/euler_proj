'''
Created on 2012-9-23

@author: csee
'''

import mtools
import unittest
import time

def get_n(p1, p2):
    d = mtools.count_digits(p1)
    a = 1
    while True:
        n = a*(10**d) + p1 
        if n % p2 != 0:
            a += 1
        else:
            b = n / p2
            print 'p1=%s p2=%s a=%s b=%s n=%s' % (p1, p2, a, b, n)
            return n

def sum_n(lim):
    s = 0
    _ps = mtools.sieve_primes(lim+1)
    ps = _ps[2:]
    for i in range(len(ps)-1):
        n = get_n(ps[i], ps[i+1])
        s += n
    return s

def solve():
    return sum_n(1000)

class TP(unittest.TestCase):
    def test_min_d(self):
        pass

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
