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
    dd = 10**d
    while True:
        n = a*dd + p1 
        if n % p2 != 0:
            a += 1
        else:
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
    return sum_n(1000000)

class TP(unittest.TestCase):
    def test_sum_n(self):
        self.assertEqual(59358, sum_n(100))
        
if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
