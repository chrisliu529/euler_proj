'''
Created on 2012-7-28

@author: EvieChris
'''

import mtools
import unittest

arr = [i*i for i in range(7073)]

def sum_palindromic_below(lim):    
    i = 1
    lst = []
    while True:
        c = i+2
        s = sum(arr[i:c])
        if s > lim:
            return sum(mtools.unique(lst))
        while s <= lim:
            if mtools.is_palindrome(s):
                lst.append(s)
            s += arr[c]
            c += 1            
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
