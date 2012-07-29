'''
Created on 2012-7-29

@author: EvieChris
'''

import mtools
import unittest

visited = {}

def m(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    try:
        return visited[n]
    except KeyError:
        res = m0(n)
        visited[n] = res
        return res

def m0(n):
    if mtools.is_prime(n):
        res = m(n-1) + 1
    else:
        p, c = mtools.prime_factors(n)
        res = sum([x*m(p[i]) for (i, x) in enumerate(c)])
    print n, res
    return res

class TP(unittest.TestCase):
    def test_m(self):
        #known condition
        self.assertEqual(5, m(15))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        l = ([m(i) for i in range(2, 201)])
        print l
        return sum(l)

if __name__ == "__main__":
    mtools.run(P())
