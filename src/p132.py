'''
Created on 2012-10-15

@author: chrisliu
'''

import mtools
import unittest
import time

def solve():
    factors_fun = [lambda x: x+1,
                   lambda x: (x**2+1),
                   lambda x: (x**4+1),
                   lambda x: (x**4-x**3+x**2-x+1),
                   lambda x: (x**4+x**3+x**2+x+1),
                   lambda x: (x**8+1),
                   lambda x: (x**8-x**6+x**4-x**2+1),
                   lambda x: (x**16+1),
                   lambda x: (x**16-x**12+x**8-x**4+1),
                   lambda x: (x**20-x**15+x**10-x**5+1),
                   lambda x: (x**20+x**15+x**10+x**5+1),
                   lambda x: (x**32-x**24+x**16-x**8+1),
                   lambda x: (x**32+1)]
    factors = [x(10) for x in factors_fun]
    l = []
    for fc in factors:
        print fc
        primes, count = mtools.prime_factors(fc)
        for (p, c) in zip(primes, count):            
            l += [p]*c
        l.sort()
        print len(l), l
        if len(l) >= 40:
            break
    return sum(l[:40])

class TP(unittest.TestCase):
    pass

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
