'''
Created on 2012-9-18

@author: chrisliu
'''

import mtools
import unittest
import time

def normalize(e, d):
    g = mtools.gcd(e, d)
    return e/g, d/g  

def min_d(m, n):
    i = 4
    while i < 100:
        ps, c = mtools.prime_factors(i)
        pm = mtools.mul(ps)
        pm1 = mtools.mul([p-1 for p in ps])
        e = i*pm1
        d = (i-1)*pm
        e1,d1 = normalize(e, d)
        v1 = e1*n
        v2 = d1*m
        print i, e1, d1
        if v1 < v2:
            return i
        i += 1

def solve():
    return min_d(15499,94744)

class TP(unittest.TestCase):
    def test_min_d(self):
        self.assertEqual(12, min_d(2,5))

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
