'''
Created on 2012-7-16

@author: chrisliu
'''

import mtools
import unittest

def f(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 3
    return 3*(n-2)

visited = {}

def g(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return f(n)

    #avoid repeatedly calculation 
    try:
        return visited[n]
    except KeyError:
        ret = f(n)
        for m in range(2,5):
            for j in range(n-m+1):
                ret += g(j)
        visited[n] = ret
        return ret

def fill(n):
    return 1 + g(n)

class TestP117(unittest.TestCase):
    def test_g(self):
        self.assertEqual(1, g(2))
        self.assertEqual(3, g(3))
        self.assertEqual(7, g(4))
        
    def test_fill(self):
        #p117 known condition
        self.assertEqual(15, fill(5))
        
class P117:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP117)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return fill(50)

if __name__ == "__main__":
    mtools.run(P117())
