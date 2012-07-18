'''
Created on 2012-7-18

@author: csee
'''

import mtools
import unittest

'''
Estimate the searching scale first
'''
class TestP118(unittest.TestCase):
    def test_1(self):
        n = mtools.mul(range(1,10))
        print n

class P118:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP118)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        pass

if __name__ == "__main__":
    mtools.run(P118())
