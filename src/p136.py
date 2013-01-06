import unittest
import time
from math import sqrt
import itertools

testing = 0
def init(t):
    global testing
    testing = t
init(0)

class TP(unittest.TestCase):
    def test_solutions(self):
        self.assertEqual(25, solutions(100))

def solutions(n):
    L = [0 for x in range(n)]
    z = 1
    while z < n:
        d = int(z/3) + 1
        while d < n:
            t = (d+z)*(3*d-z)
            if t >= n:
                break
            L[t] += 1
            d += 1
        z += 1
    s = 0
    for x in L:
        if x == 1:
            s += 1
    return s

if testing:
    unittest.main()

def solve():
    return solutions(50000000)

if not testing:
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
