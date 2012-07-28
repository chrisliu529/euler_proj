'''
Created on 2012-7-28

@author: EvieChris
'''

import mtools
import unittest

arr = [i*i for i in range(7073)]

def sum_palindromic_below(lim):    
    l = 2
    S = 0
    i = 1
    while True:
        s = sum(arr[i:i+l])
        if s > lim:
            if i == 1:
                return S
            l += 1
            i = 1
        else:
            if mtools.is_palindrome(s):
                print s,i,l
                S += s
            i += 1

class TP(unittest.TestCase):
    def test_sum_palindromic_below(self):
        #known condition
        self.assertEqual(4164, sum_palindromic_below(1000))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return sum_palindromic_below(10**8)

if __name__ == "__main__":
    mtools.run(P())
