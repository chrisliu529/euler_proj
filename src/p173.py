'''
Created on 2012-8-18

@author: csee
'''

import unittest
import time
import math

def search(N):
    return sum([(int(math.sqrt(m*m+N)-m)/2) for m in range(1, N/4)])

def solve():
    return search(10**6)

class TP(unittest.TestCase):
    def test_search(self):
        #known condition
        self.assertEqual(41, search(100))

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
