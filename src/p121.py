'''
Created on 2012-8-27

@author: chrisliu
'''

import unittest
import time
import mtools

def bounds(n):
    return n/2+1, n 

def fund(n):
    lower, upper = bounds(n)
    p = 0
    for b in range(lower, upper+1):
        r = n - b
        for seq in mtools.comb(range(1,n+1), r):
            a = mtools.mul(seq)
            p += a
    return mtools.fac(n+1)/p

def solve():
    return fund(15)

class TP(unittest.TestCase):
    def test_bounds(self):
        self.assertEqual((3,4), bounds(4))
        self.assertEqual((8,15), bounds(15))

    def test_fund(self):
        #known condition
        self.assertEqual(10, fund(4))

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
