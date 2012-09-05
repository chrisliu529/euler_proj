'''
Created on 2012-9-5

@author: csee
'''

import mtools
import unittest
import time

def a1(n):
    if n == 1:
        return 1
    return a0(n-1)

def a0(n):
    if n == 1:
        return 2
    return g(n-1) + h(n-1)

htab = {1:2}

def h(n):
    try:
        return htab[n]
    except KeyError:
        res = h(n-1) + a0_(n-1) + a1_(n-1)
        htab[n] = res
        return res

def a0_(n):
    if n == 1:
        return 1
    return h(n-1)

def a1_(n):
    if n == 1:
        return 1
    return a0_(n-1)

gtab = {1:3}

def g(n):
    try:
        return gtab[n]
    except KeyError:
        res = g(n-1) + h(n-1) + a0(n-1) + a1(n-1)
        gtab[n] = res
        print gtab
        return res

def solve():
    return g(30)

class TP(unittest.TestCase):
    def test_g(self):
        self.assertEqual(43, g(4))
    
if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
