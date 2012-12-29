import time
import unittest

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def sieve(n):
    l = [1 for x in range(0,n)]
    for i in range(2,n):
        if l[i] == 1:
            l[i] = i
            for j in range(i+i,len(l),i):
                l[j] *= i
    return l

radicals = sieve(120000)

def sum_c(N):
    au = int(N/2+0.5)
    s = 0
    for a in range(1,au):
	if a % 1000 == 0:
            print a
        for b in range(a+1, N-a):
            c = a+b
            if radicals[a]*radicals[b]*radicals[c] < c and gcd(a,b) == 1:
                s += c
    return s

def solve():
    return sum_c(120000)

class TP(unittest.TestCase):
    def test_rad(self):
        self.assertEqual(42, rad(504))
        self.assertEqual(30, rad(4320))

    def test_sum_c(self):
        self.assertEqual(12523, sum_c(1000))

testing = 0

def init(t):
    global testing
    testing = t
init(0)

if testing:
    unittest.main()
else:
    t = time.time()
    answer = solve()
    t2 = time.time()
    print "answer = %s" % answer 
    print "(%s)" % (t2 - t)
