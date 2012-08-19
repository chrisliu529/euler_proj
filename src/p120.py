'''
Created on 2012-7-24

@author: chrisliu
'''

import mtools
import unittest

def r_max(a):
    if a%2 == 0:
        return a*(a-2)
    return a*(a-1) 

def get_answer():
    return sum([r_max(i) for i in range(3, 1001)])

class TP(unittest.TestCase):
    def test_r_max(self):
        self.assertEqual(42, r_max(7))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
