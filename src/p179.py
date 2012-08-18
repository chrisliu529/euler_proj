'''
Created on 2012-8-18

@author: csee
'''

import mtools
import unittest

def search(upper):
    cnt = 0
    v1 = mtools.factors_count(2)
    for n in range(2, upper+1):
        v2 = mtools.factors_count(n+1)
        if v1 == v2:
            cnt += 1
        v1 = v2
    return cnt

def get_answer():
    return search(10**7)

class TP(unittest.TestCase):
    pass

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
