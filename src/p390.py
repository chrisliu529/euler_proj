'''
Created on 2012-6-30

@author: csee
'''

import mtools
import unittest
from math import sqrt

def is_good_factor(p):
    # p = 4*m^2+1
    return p >= 5 and (p-1) % 4 == 0 and mtools.is_int_sqrt((p-1)/4)

def S(x):
    res = 0
    for N in range(9, 10**x):
        T = 4*N*N + 1
        factors = mtools.factors(T)
        factors.sort()
        for p in factors:
            if is_good_factor(p):
                q = T/p
                if is_good_factor(q):
                    print sqrt(p-1)/2, sqrt(q-1)/2, N
                    res += N
    return res

class TestP390(unittest.TestCase):
    def test1(self):
        #self.assertEqual(18018206, S(4))
        pass

class P390:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP390)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return S(4)

if __name__ == "__main__":
    mtools.run(P390())
