'''
Created on 2012-9-11

@author: csee
'''

import mtools
import unittest
import time

def solve_n(lim):
    m = 1
    cnt = 0
    while True:
        p = 3*m*m + 3*m + 1
        if p >= lim:
            return cnt
        if mtools.is_prime(p):
            cnt += 1
        m += 1

def solve():
    return solve_n(10**6)

class TP(unittest.TestCase):
    def test_solve_n(self):
        self.assertEqual(4, solve_n(100))

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
