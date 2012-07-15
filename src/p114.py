'''
Created on 2012-7-15

@author: csee
'''

import mtools
import unittest

def f(n, m):
    return (n-m+1)*(n-m+2)/2

visited = {}

def g(n, m):
    #avoid repeatedly calculation 
    try:
        return visited[(n,m)]
    except KeyError:
        if n < m:
            return 0
        cnt = f(n, m)
        for i in range(m, n+1):
            for j in range(n-i+1):
                cnt += g(j-1, m)
        visited[(n,m)] = cnt
        return cnt

def fill(n, m):
    return 1 + g(n,m)

class TestP114(unittest.TestCase):
    def test1(self):
        self.assertEqual(17, fill(7, 3), "p114 known condition")
        
    def test2(self):
        self.assertEqual(673135, fill(29, 3), "p115 known condition")
        self.assertEqual(1089155, fill(30, 3), "p115 known condition")
        pass

class P114:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP114)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return fill(50, 3)

if __name__ == "__main__":
    mtools.run(P114())
