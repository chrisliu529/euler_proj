'''
Created on 2012-8-12

@author: csee
'''

import mtools
import unittest

c = mtools.c
    
def get_answer():
    print "n     win      draw"
    for i in range(20, 101):        
        print i, win_ratio(i, 6, 100, 6), draw_ratio(i, 6, 100, 6)

def win_ratio(i1, j1, i2, j2):
    peter = ptab(i1, j1)
    colin = ptab(i2, j2)
    s = 0
    for i in range(i1, i1*j1+1):
        s += peter[i]*sum([colin[j] for j in range(i2, i)])
    t = (j1**i1)*(j2**i2)
    return '%.7f' % (float(s)/t)

def draw_ratio(i1, j1, i2, j2):
    peter = ptab(i1, j1)
    colin = ptab(i2, j2)
    s = 0
    m = n = 0
    if i1 < i2:
        m = i2
    else:
        m = i1
    if i1*j1 < i2*j2:
        n = i1*j1
    else:
        n = i2*j2 
    for i in range(m, n):
        s += peter[i]*colin[i]
    t = (j1**i1)*(j2**i2)
    return '%.7f' % (float(s)/t)

def ptab(i, j):
    d = {}
    for n in range(i, j*i+1):
        d[n] = state_num(i, j, n)
    return d

def state_num(i, j, n):
    s = c(n-1, i-1)
    for k in range(1, i+1):
        v = c(i, k)*a(k, i, j, n)
        if k % 2 == 0:
            s += v
        else:
            s -= v
    return s

def a(k, i, j, n):
    return c(n-k*j-1, i-1)

t94 = {9: 1, 10: 9, 11: 45, 12: 165, 13: 486, 14: 1206, 15: 2598, 16: 4950, 17: 8451, 18: 13051, 19: 18351, 20: 23607, 21: 27876, 22: 30276, 23: 30276, 24: 27876, 25: 23607, 26: 18351, 27: 13051, 28: 8451, 29: 4950, 30: 2598, 31: 1206, 32: 486, 33: 165, 34: 45, 35: 9, 36: 1}
t66 = {6: 1, 7: 6, 8: 21, 9: 56, 10: 126, 11: 252, 12: 456, 13: 756, 14: 1161, 15: 1666, 16: 2247, 17: 2856, 18: 3431, 19: 3906, 20: 4221, 21: 4332, 22: 4221, 23: 3906, 24: 3431, 25: 2856, 26: 2247, 27: 1666, 28: 1161, 29: 756, 30: 456, 31: 252, 32: 126, 33: 56, 34: 21, 35: 6, 36: 1}

class TP(unittest.TestCase):
    def test_ptab(self):
        self.maxDiff = None
        self.assertEqual(t94, ptab(9,4))
        self.assertEqual(t66, ptab(6,6))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
