'''
Created on 2012-7-15

@author: csee
'''

import mtools
import unittest
from p114 import fill

def search_min(n, lim):
    high = n
    while fill(high, n) < lim:
        high *= 2
    low = high/2
    while True:
        n1 = (high+low)/2
        v = fill(n1, n)
        if v < lim:
            low = n1+1
        elif v > lim:
            high = n1-1
        else:
            return n1
        n2 = (high+low)/2
        if n1 == n2:
            if high > low:
                return high
            return low

class TestP115(unittest.TestCase):
    def test1(self):
        self.assertEqual(880711, fill(56, 10), "p115 known condition")
        self.assertEqual(1148904, fill(57, 10), "p115 known condition")

    def test_search_min(self):
        self.assertEqual(57, search_min(10, 1000000))

class P115:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP115)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return search_min(50, 1000000)

if __name__ == "__main__":
    mtools.run(P115())
