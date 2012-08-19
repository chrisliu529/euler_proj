'''
Created on 2012-7-18

@author: csee
'''

import mtools
import unittest

def trunc_number(n, i, j):
    l = []
    while j >= i:
        s = mtools.separate_digits(n)
        m = int(mtools.combine_digits(s[:i]))
        r = int(mtools.combine_digits(s[i:]))
        if r > m:
            l.append((m, r))
        i += 1
    return l

def is_prime(n):
    return mtools.is_prime(n)

def count_partition(n):
    stack = [(1, n, [])]
    cnt = 0
    ls = []
    while stack:
        p, r, l = stack.pop()
        j = mtools.count_digits(p)
        k = mtools.count_digits(r)
        for (m,r1) in trunc_number(r, j, k/2):
            l2 = l[:]
            if m > p and is_prime(m):
                l2.append(m)
                stack.append((m, r1, l2))
                if r1 > m and is_prime(r1):
                    l3 = l2[:]
                    l3.append(r1)
                    cnt += 1
                    ls.append(l3)
    return cnt, ls

def hashable(l):
    return ','.join([str(x) for x in l])

def count():
    l = range(1,10)
    cnt = 0
    sets = []
    for np in mtools.dict_perm(l):
        if np[-1] in [2,4,5,6,8]:
            continue
        n = mtools.combine_digits(np)
        c, s = count_partition(n)
        cnt += c
        if c > 0:
            for e in s:
                sets.append(e)
    
    #output all valid sets and
    #make sure no duplicates 
    d = {}
    for s in sets:
        h = hashable(s)
        try:
            if d[h]:
                print h
                return 'Duplicated.'
        except KeyError:
            print h
            d[h] = True                        
    return cnt

class TestP118(unittest.TestCase):
    def test_trunc_number(self):
        numbers = trunc_number(254789631, 1, 4)
        self.assertEqual(4, len(numbers))
        self.assertEqual((2, 54789631), numbers[0])
        self.assertEqual((2547, 89631), numbers[3])

    def test_count_partition(self):
        c, s = count_partition(127859463)
        self.assertEqual(0, c)
        c, s = count_partition(127643859)
        self.assertEqual(2, c)

class P118:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP118)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return result.wasSuccessful()

    def solve(self):
        return count()

if __name__ == "__main__":
    mtools.run(P118())
