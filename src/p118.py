'''
Created on 2012-7-18

@author: csee
'''

import mtools
import unittest

def search_8():
    l = range(1,10)
    pl = [2,3,5,7]
    cnt = 0
    for x in pl:
        l2 = l[:]
        del l2[x-1]
        for np in mtools.dict_perm(l2):
            n = mtools.combine_digits(np)
            if mtools.is_prime(n):
                print x, n
                cnt += 1
    return cnt

def make_dict():
    primes = mtools.sieve_primes(10**7)
    print len(primes)

def search_other():
    d = make_dict()

def trunc_number(n, i, j):
    l = []
    while j >= i:
        s = mtools.separate_digits(n)
        m = int(mtools.combine_digits(s[:i]))
        r = int(mtools.combine_digits(s[i:]))
        l.append((m, r))
        i += 1
    return l

def is_prime(n):
    return mtools.is_prime(n)

def count_partition(n):
    stack = [(1, n)]
    cnt = 0
    while stack:
        #print stack
        p, r = stack.pop()
        j = mtools.count_digits(p)
        k = mtools.count_digits(r)
        for (m,r1) in trunc_number(r, j, k/2):
            if m > p and is_prime(m):
                stack.append((m, r1))
                if is_prime(r1):
                    print r1
                    cnt += 1
    return cnt

def count():
    l = range(1,10)
    cnt = 0
    i = 0
    for np in mtools.dict_perm(l):
        if np[-1] in [2,4,5,6,8]:
            continue
        n = mtools.combine_digits(np)
        c = count_partition(n)
        print np, c
        cnt += c
        i += 1
    print "i=%s" % i
    return cnt

class TestP118(unittest.TestCase):
    def test_1(self):
        #n = search_8()
        #print "number of (1,8) sets=", n
        #n = search_other()
        #print "number of other sets=", n
        #n = count_partition(254789631)
        #print n
        pass

    def test_trunc_number(self):
        numbers = trunc_number(254789631, 1, 4)
        self.assertEqual(4, len(numbers))
        self.assertEqual((2, 54789631), numbers[0])
        self.assertEqual((2547, 89631), numbers[3])
        numbers = trunc_number(54789631, 1, 4)
        print numbers

    def test_count_partition(self):
        self.assertEqual(1, count_partition(254789631))
        self.assertEqual(2, count_partition(978534621))
        self.assertEqual(0, count_partition(194236857))        

class P118:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP118)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return count()
        #pass

if __name__ == "__main__":
    mtools.run(P118())
