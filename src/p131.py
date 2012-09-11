'''
Created on 2012-9-11

@author: csee
'''

import mtools
import math
import unittest
import time

def solve_n(lim):
    ns = [x**3 for x in range(600+1)]
    ps = mtools.sieve_primes(lim)
    ps.reverse()
    cnt = 0
    t = time.time()
    for p in ps:
        for n in ns:
            np = n + p
            if is_cubic(np):
                print math.pow(n, 1/3.0), p, time.time() - t
                cnt += 1
                break
    return cnt

def is_cubic(n):
    t = math.pow(n, 1/3.0)
    d = abs(t-int(t))
    return d < 0.00000001 or 1-d < 0.00000001 

def solve():
    return solve_n(10**6)

class TP(unittest.TestCase):
    def test_solve_n(self):
        self.assertEqual(4, solve_n(100))
    
    def test_is_cubic(self):
        self.assertTrue(is_cubic(8))
        self.assertTrue(is_cubic(409**3))
        self.assertFalse(is_cubic(409**3+5))
        self.assertFalse(is_cubic(4099**3+5))
        self.assertTrue(is_cubic(4099**3))

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
