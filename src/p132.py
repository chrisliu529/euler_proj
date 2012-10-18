'''
Created on 2012-10-15

@author: chrisliu
'''

import mtools
import unittest
import time

def solve():
    ps = mtools.sieve_primes(10**6)
    n = 10**9
    res = []
    for p in ps:
        if p < 7:
            continue
        if pow(10, n, p) == 1:
            res.append(p)
        if len(res) == 40:
            print res
            return sum(res)

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
