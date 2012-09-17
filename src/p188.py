'''
Created on 2012-9-15

@author: csee
'''

import mtools
import unittest
import time
import sys

def hyper_exp_mod(a, b, m):
    if m == 1:
        return a
    if b == 1:
        return a % m
    return pow(a, hyper_exp_mod(a, b-1, mtools.phi(m)), m)

def solve():
    return hyper_exp_mod(1777, 1855, 10**8)

class TP(unittest.TestCase):
    def test_hyper_exp_mod(self):
        self.assertEqual(87, hyper_exp_mod(3, 3, 10**2))
        self.assertEqual(4987, hyper_exp_mod(3, 3, 10**4))

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
