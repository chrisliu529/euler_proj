'''
Created on 2012-6-30

@author: csee
'''

import mtools
import unittest
from math import sqrt
import time

def count(n):
    cm = int(sqrt(n/2))
    c = 1
    s = 0
    while c <= cm:
        c2 = c*c
        bm = int(sqrt(n*n-c2)/sqrt(4*c2+1))
        b = c+1
        while b <= bm:
            b2 = b*b
            a2 = 4*b2*c2+b2+c2
            if mtools.is_square(a2):
                a = int(sqrt(a2))
                print c,b,a
                s += int(sqrt(a2))
            b += 1
        c += 1
    return s

def solve():
    return count(10**7)

class TP(unittest.TestCase):
    def test_count(self):
        self.assertEqual(9, count(10))
        self.assertEqual(18018206, count(10**6))
    
if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
