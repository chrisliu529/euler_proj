'''
Created on 2012-8-18

@author: EvieChris
'''

import mtools
import unittest
import math

def get_answer():
    return count_semi_primes(10**8)

def count_semi_primes(n):
    pt = mtools.sieve_primes(n/2 + 1)
    i = 0
    cur = len(pt) - 1
    cnt = 0
    while i <= cur:
        p = pt[i]
        while pt[cur]*p >= n:
            cur -=1
        cnt += (cur-i+1)
        i += 1
    return cnt        

def direct_search(upper):
    cnt = 0
    for n in range(4, upper):
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                if mtools.is_prime2(i):
                    t = n / i
                    if mtools.is_prime2(t):
                        cnt += 1
    return cnt

class TP(unittest.TestCase):
    def test_direct_search(self):
        self.assertEqual(3, direct_search(10))
        self.assertEqual(10, direct_search(27))
        
    def test_count_semi_primes(self):
        cases = [10, 27, 100, 1000]
        for i in cases:
            self.assertEqual(count_semi_primes(i), direct_search(i))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
