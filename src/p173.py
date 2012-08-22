'''
Created on 2012-8-22

@author: chrisliu
'''

import unittest

class TP(unittest.TestCase):
    def test_direct_search(self):
        self.assertEqual(3, direct_search(10))
        self.assertEqual(10, direct_search(27))
        
    def test_count_semi_primes(self):
        cases = [10, 27, 100, 1000]
        for i in cases:
            self.assertEqual(count_semi_primes(i), direct_search(i))

if __name__ == "__main__":
    solve()
