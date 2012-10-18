'''
Created on 2012-10-15

@author: chrisliu
'''

import mtools
import unittest
import time

fv = {}

def R(n):
    return (10**n - 1)/9

def prime_factors(n):
    ps, _ = mtools.prime_factors(n)
    return ps

def solve():
    return collect_primes(10*9, 40)

def collect_primes1(n):
    pl = []
    fl = mtools.factors(n)
    fl.sort()
    print n, fl
    r = R(n)
    for f in fl:
        if f != n:
            t = r / R(f)
            pl += prime_factors(t)
    return mtools.unique(pl)

def collect_primes(n, m):
    pl = []
    fl = mtools.factors(n)
    fl.sort()
    for f in fl:
        try:
            if fv[f]:
                continue
        except KeyError:
            pl += collect_primes1(f)
            pl = mtools.unique(pl)
            pl.sort()
            print f, pl, fv
            if len(pl) >= m:
                return sum(pl[:m])
            fv[f] = True 

class TP(unittest.TestCase):
    def test_R(self):
        self.assertEqual(11, R(2))
        self.assertEqual(1111, R(4))
    
    def test_collect_primes(self):
        self.assertEqual(9414, collect_primes(10, 4))

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
