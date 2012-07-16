'''
Created on 2012-7-16

@author: chrisliu
'''

import mtools
import unittest

def f(n, m):
    if n < m:
        return 0
    return n-m+1

visited = {}

def g(n, m):
    #avoid repeatedly calculation 
    try:
        return visited[(n,m)]
    except KeyError:
        ret = f(n, m)
        for i in range(n-m+1):
            ret += g(i, m)
        visited[(n,m)] = ret
        return ret

def fill2(n):
    return sum([g(n, i) for i in range(2,5)])

class TestP116(unittest.TestCase):
    def test_g(self):
        #p116 known condition
        self.assertEqual(7, g(5,2))
        self.assertEqual(3, g(5,3))
        self.assertEqual(2, g(5,4))

    def test_fill2(self):
        #p116 known condition
        self.assertEqual(12, fill2(5))
        
class P116:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP116)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return fill2(50)

if __name__ == "__main__":
    mtools.run(P116())
