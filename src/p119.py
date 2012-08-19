'''
Created on 2012-7-23

@author: chrisliu
'''

import mtools
import unittest

def has_property(n, m):
    return n == sum(mtools.separate_digits(m))

def search():
    l = []
    for i in range(2,100):
        for j in range(2,i):
            n = i**j
            if has_property(i, n):
                l.append(n)
    l.sort()
    return l[29]

class TP(unittest.TestCase):
    def test_has_property(self):
        self.assertTrue(has_property(8, 512))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return search()

if __name__ == "__main__":
    mtools.run(P())
