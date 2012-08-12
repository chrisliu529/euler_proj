'''
Created on 2012-8-12

@author: csee
'''

import mtools
import unittest
import random

def get_answer():
    times = 0
    win = 0
    while True:
        times += 1
        if peter() > colin():
            win += 1
            if times % 1000000 == 0:
                print '%s: %s' % (times/100, float(win)/times)

def peter():
    return roll_dice(9, 4)

def colin():
    return roll_dice(6, 6)

def roll_dice(n, m):
    s = 0
    for i in range(n):
        s += random.randint(1, m)
    return s

class TP(unittest.TestCase):
    def test_xx(self):
        pass

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
