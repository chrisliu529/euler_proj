'''
Created on 2012-8-19

@author: csee
'''

import mtools
import unittest

c = mtools.c

def get_answer():
    return direct_search(51)

def direct_search(row):
    d = {}
    for i in range(1, row):
        u = up(i)
        for j in range(u+1):
            try:
                v = c(i, j)
                if d[v]:
                    continue
            except KeyError:
                d[v] = True
    l = d.keys()
    return sum([k for k in l if square_free(k)])
                
def square_free(n):
    i = 2
    while (n > 1) and (i*i <= n):
        if n % i == 0:
            c = 0
            while (n%i == 0):
                c += 1
                if c == 2:
                    return False
                n /= i
        i += 1
    return True

def up(i):
    j = i/2
    if i % 2 == 0:
        return j
    return j + 1

class TP(unittest.TestCase):
    def test_direct_search(self):
        self.assertEqual(105, direct_search(8))
        
    def test_up(self):
        self.assertEqual(2, up(3))
        self.assertEqual(2, up(4))
        
    def test_square_free(self):
        self.assertEqual(True, square_free(1))
        self.assertEqual(True, square_free(2))
        self.assertEqual(True, square_free(10))
        self.assertEqual(False, square_free(4))
        self.assertEqual(False, square_free(20))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
