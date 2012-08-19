'''
Created on 2012-6-24

@author: csee
'''

import mtools
import unittest

def f(x, y):
    return mtools.c(x+y-1, y)

def count_not_bouncy(m, n):
    return sum([f(m, y) for y in range(1,n+1)]) \
        + sum([f(x, y) for x in range(1,m+1) for y in range(1, n+1)]) \
        - n*m

class TestP113(unittest.TestCase):
    def test1(self):
        self.assertEqual(12951, count_not_bouncy(6, 9))
    def test2(self):
        self.assertEqual(277032, count_not_bouncy(10, 9))

class P113:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP113)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return count_not_bouncy(100, 9)

if __name__ == "__main__":
    mtools.run(P113())
