'''
Created on 2012-7-29

@author: EvieChris
'''

import mtools
import unittest

def get_answer():
    f = file('b003313.txt')
    i = 0
    n = 0
    for line in f:
        l = line.strip().split(' ')
        n += int(l[1])
        i += 1
        if i == 200:
            return n

class TP(unittest.TestCase):
    def test_m(self):
        pass

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
