'''
Created on 2012-9-23

@author: csee
'''

import mtools
import unittest
import time
import math

def euclidean(a, b):
    lq = []
    while b != 1:
        t = b
        lq.append(a/b)
        b = a % b
        a = t
    n = len(lq)
    if n % 2 == 0:
        return -Q(n, lq), P(n, lq)
    return Q(n, lq), -P(n, lq)

def P(k, lq):
    p0 = 1
    p1 = lq[0]
    i = 2
    p = 0
    while i < k:
        p = lq[i-1]*p1 + p0
        p0 = p1
        p1 = p
    return p

def Q(k, lq):
    q0 = 0
    q1 = 1
    i = 2
    q = 0
    while i < k:
        q = lq[i-1]*q1 + q0
        q0 = q1
        q1 = q
    return q
    
def get_n(p1, p2):
    d = mtools.count_digits(p1)
    dd = 10**d
    _, b0 = euclidean(dd, p2)
    t = math.floor(-p1*b0/dd)
    b = - (p1*b0 + dd*t)
    assert b > 0
    return b*p2

def sum_n(lim):
    s = 0
    _ps = mtools.sieve_primes(lim+1)
    ps = _ps[2:]
    for i in range(len(ps)-1):
        n = get_n(ps[i], ps[i+1])
        s += n
    return s

def solve():
    return sum_n(1000000)

class TP(unittest.TestCase):
    def test_sum_n(self):
        self.assertEqual(59358, sum_n(100))
        
if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
