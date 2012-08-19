'''
Created on 2012-8-18

@author: csee
'''

import mtools
import unittest

def search(upper):
    cnt = 0
    l = [0 for x in range(0,upper)]
    lim = upper/2
    for i in range(2,lim):
        for j in range(i,len(l),i):
            l[j] += 1
    for i in range(2,len(l)-1):
        if l[i] == l[i+1]:
            cnt += 1
    return cnt

def get_answer():
    return search(10**7)
    pass

class TP(unittest.TestCase):
    def test_search(self):
        #sure results with direct search
        self.assertEqual(15, search(100))
        self.assertEqual(118, search(1000))
        self.assertEqual(10585, search(100000))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
