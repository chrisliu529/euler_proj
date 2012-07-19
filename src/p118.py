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

class TestP118(unittest.TestCase):
    def test_1(self):
        n = search_8()
        print "number of (1,8) sets=", n
        #n = search_other()
        #print "number of other sets=", n

class P118:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP118)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        pass

if __name__ == "__main__":
    mtools.run(P118())
