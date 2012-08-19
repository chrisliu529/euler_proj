'''
Created on 2012-8-10

@author: chrisliu
'''

import mtools
import unittest
import math

def get_answer():
    l = nth_pd(3, 2000)
    return l[1999]

def nth_pd(m, n):
    l = [1,2]
    i = 1
    while True:
        t = s(i)
        for j in range(2):
            v = t+j
            k = pd(v)
            if k == m:
                l.append(v)
                if len(l) == n:
                    return l
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

first100 = [1, 2, 8, 19, 20, 37, 61, 128, 217, 271, 398, 919, 1519, 1520, 2978, 3170, 4220, 4447, 4681, 5677, 5941, 6488, 8269, 9920, 10621, 12481, 16651, 17558, 22448, 26227, 29701, 34028, 34669, 35317, 35971, 56719, 60920, 61777, 74419, 75367, 80197, 88238, 93458, 110018, 117019, 125461, 136747, 140618, 156637, 169220, 172081, 174968, 182288, 183769, 185257, 214670, 216277, 217891, 246248, 265520, 292970, 302419, 331670, 333667, 362269, 370658, 381278, 407377, 416270, 486019, 498169, 540601, 558578, 590077, 600770, 606151, 672607, 704221, 882920, 1000519, 1053170, 1092637, 1121798, 1181269, 1181270, 1203967, 1215398, 1277269, 1277270, 1281187, 1285111, 1332668, 1340677, 1510171, 1566020, 1627298, 1671788, 1698770, 1703287, 1790270]

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
        self.assertEqual(first100[:10], nth_pd(3, 10))
        self.assertEqual(first100, nth_pd(3, 100))

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return get_answer()
        #pass

if __name__ == "__main__":
    mtools.run(P())
