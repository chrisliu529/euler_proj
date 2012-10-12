'''
Created on 2012-10-12

@author: chrisliu
'''

import mtools
import unittest
import time
import math

def solve():
    d = {}
    t = 2
    while t <= 250000:
        n = get_n(t)
        try:
            d[n] += 1
        except KeyError:
            d[n] = 1
        t += 1
    assert d[15] == 832 #known condition
    return sum([d[i] for i in range(1, 11)])

def get_n(t):
    return mtools.factors_count(t)/2
    
class TP(unittest.TestCase):
    def test_get_n(self):
        self.assertEqual(1, get_n(2))
        self.assertEqual(1, get_n(4))
        self.assertEqual(2, get_n(8))

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
