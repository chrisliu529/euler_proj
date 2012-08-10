'''
Created on 2012-8-10

@author: chrisliu
'''

import mtools
import unittest
import math

def get_answer():
    return nth_pd(3, 2000)

def nth_pd(m, n):
    cnt = 1 #pd(1) == 3 
    i = 2
    while True:
        k = pd(i)
        if k == m:
            cnt += 1
            print i, cnt
            if cnt == n:
                return i
        i += 1

def pd(n):
    l = neighbors(n)
    l2 = [abs(n-x) for x in l]
    cnt = 0
    for x in l2:
        if mtools.is_prime(x):
            cnt += 1
    return cnt

def s(i):
    return 1+3*i*(i+1)

def u(i):
    return s(i-1) + 1

def mr(r, x, n):
    if x == 1:
        return [n+1, s(r)]
    if x == 6*r:
        return [u(r), n-1]
    return [n-1, n+1]

def ier(r, x):
    v = iv1 = iv2 = ev1 = ev2 = ev3 = 0
    d = (x-1) / r
    m = (x-1) % r
    if r == 1:
        v = 1
    else: 
        v = u(r-1) + (r-1)*d
    if m == 0:
        if (x == 1):
            ev1 = s(r+1)
            ev2 = u(r+1)
            ev3 = ev2 + 1
        else:
            ev2 = u(r+1) + (r+1)*d
            ev1 = ev2 - 1
            ev3 = ev2 + 1
        return [v, ev1, ev2, ev3]
    else:
        iv1 = v + m
        iv2 = iv1 - 1
        if (iv1 > s(r-1)):
            iv1 = u(r-1) 
        _ev2 = u(r+1) + (r+1)*d
        ev1 = _ev2 + m
        ev2 = ev1 + 1
        return [iv1, iv2, ev1, ev2]

def neighbors(n):
    r,x = loc(n)
    l = mr(r, x, n) + ier(r, x)
    l.sort()
    return l

def loc(n):
    r = int(math.ceil((math.sqrt(12*n-3)-3)/6))
    x = n-(1+3*r*(r-1))
    return (r,x)

class TP(unittest.TestCase):
    def test_loc(self):
        self.assertEqual((1,1), loc(2))
        self.assertEqual((2,1), loc(8))
        self.assertEqual((2,12), loc(19))
        self.assertEqual((3,1), loc(20))
        self.assertEqual((1,3), loc(4))
        self.assertEqual((3,4), loc(23))
        self.assertEqual((3,18), loc(37))
        
    def test_s(self):
        self.assertEqual(7, s(1))
        self.assertEqual(19, s(2))
        self.assertEqual(37, s(3))

    def test_u(self):
        self.assertEqual(2, u(1))
        self.assertEqual(8, u(2))
        self.assertEqual(20, u(3))

    def test_neighbors(self):
        self.assertEqual([1,3,7,8,9,19], neighbors(2))
        self.assertEqual([1,2,4,9,10,11], neighbors(3))
        self.assertEqual([2,7,8,18,36,37], neighbors(19))

    def test_pd(self):
        self.assertEqual(3, pd(8))
        self.assertEqual(2, pd(17))
        
    def test_nth_pd(self):
        self.assertEqual(271, nth_pd(3, 10))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
