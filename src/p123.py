'''
Created on 2012-7-25

@author: chrisliu
'''

import mtools
import unittest

def r(p, n):
    if n % 2 == 0:
        return 2
    p2 = p*p
    return 2*n*p % p2

def first_exceeds(lim):
    n = 5
    i = 11
    while True:
        i += 2
        if mtools.is_prime(i):
            n += 1
            if r(i, n) > lim:
                return n

def get_answer():
    return first_exceeds(10**10)

class TP(unittest.TestCase):
    def test_r(self):
        self.assertEqual(5, r(5,3))
        
    def test_first_exceeds(self):
        self.assertEqual(7037, first_exceeds(10**9))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
