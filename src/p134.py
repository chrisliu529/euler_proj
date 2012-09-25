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
    if k == 0:
        return p0
    p1 = lq[0]
    if k == 1:
        return p1
    i = 2
    p = 0
    while i <= k:
        p = lq[i-1]*p1 + p0
        p0 = p1
        p1 = p
        i += 1
    return p

def Q(k, lq):
    q0 = 0
    if k == 0:
        return q0
    q1 = 1
    if k == 1:
        return q1
    i = 2
    q = 0
    while i <= k:
        q = lq[i-1]*q1 + q0
        q0 = q1
        q1 = q
        i += 1
    return q
    
def get_n(p1, p2):
    d = mtools.count_digits(p1)
    dd = 10**d
    _, b0 = euclidean(dd, p2)
    t = int(math.floor(p1*b0/dd))
    b = p1*b0 - dd*t
    assert b > 0
    n = b*p2
    return n

def sum_n(lim):
    s = 0
    _ps = mtools.sieve_primes(lim+1)
    ps = _ps[2:]
    for i in range(len(ps)-1):
        p1 = ps[i]
        if p1 > 10**6:
            return s
        p2 = ps[i+1]
        n = get_n(p1, p2)
        s += n
    return s

def solve():
    '''
    use a range slightly larger than 10**6 to make sure p2 will be included for
    largest p1<10**6.
    '''
    return sum_n(1010000)

class TP(unittest.TestCase):
    def test_euclidean(self):
        self.assertEqual((-1, 2), euclidean(7, 4))
        self.assertEqual((9, -26), euclidean(107, 37))

    def test_get_n(self):
        self.assertEqual(1219, get_n(19, 23))

    def test_sum_n(self):
        self.assertEqual(59358, sum_n(100))
        
if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
