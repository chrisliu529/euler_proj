'''
Created on 2012-7-24

@author: chrisliu
'''

import mtools
import unittest

def r(i, n):
    return 2*(i+1)*n

def r_max(n):
    lim = n*n
    i = 1
    while r(i, n) < lim:
        i += 1
    return r(i - 1, n)

def get_answer():
    return sum([r_max(i) for i in range(3, 1001)])

class TP(unittest.TestCase):
    def test_r_max(self):
        self.assertEqual(42, r_max(7))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
