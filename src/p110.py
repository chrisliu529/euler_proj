'''
Created on 2012-7-9

@author: chrisliu
'''

import mtools
import unittest

#within the small scope defined in this problem,
#it's not possible to reach a prime factor greater than 100
#upper limit of 4M is 15th prime
primes = mtools.sieve_primes(100)

def get_n(l):
    l2 = [primes[i]**x for (i, x) in enumerate(l)]
    return mtools.mul(l2)    

def f(l):
    l2 = [2*x+1 for x in l]
    return (mtools.mul(l2)+1)/2

def inc_elem(l, i):
    l2 = list(l)
    l2[i] += 1
    return l2

def hashable(l):
    return ','.join([str(x) for x in l])

def expand_states(l):
    idx = 0
    new_states = []
    new_states.append(inc_elem(l, idx))
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            idx = i+1
            new_states.append(inc_elem(l, idx))
    new_states.append(l + [1])
    return new_states

def search(l, lim):
    states = [l]
    visited = {}
    fm = 0
    nm = 0
    while True:
        s = states.pop(0)
        h = hashable(s)
        try:
            if visited[h]:
                continue
        except KeyError:
            visited[h] = True
        fs = f(s)
        ns = get_n(s)
        if fs > lim:
            return ns
        if fs > fm:
            fm = fs
            nm = ns
        elif ns > nm:
            continue
        states += expand_states(s)
        states.sort(cmp = lambda x,y: cmp(get_n(x), get_n(y)))

class TestP110(unittest.TestCase):
    def test_get_n(self):
        self.assertEqual(2, get_n([1]))
        self.assertEqual(4, get_n([2]))
        self.assertEqual(6, get_n([1,1]))
        self.assertEqual(12, get_n([2,1]))
        self.assertEqual(30, get_n([1,1,1]))
        self.assertEqual(36, get_n([2,2]))

    def test_f(self):
        self.assertEqual(2, f([1]))
        self.assertEqual(3, f([2]))
        self.assertEqual(5, f([1,1]))
        self.assertEqual(8, f([2,1]))
        self.assertEqual(14, f([1,1,1]))
        self.assertEqual(13, f([2,2]))
        
    def test_expand_states(self):
        self.assertEqual([[2], [1,1]], expand_states([1]))
        self.assertEqual([[3], [2,1]], expand_states([2]))
        self.assertEqual([[2,1], [1,1,1]], expand_states([1,1]))
        self.assertEqual([[3,1], [2,2],[2,1,1]], expand_states([2,1]))
        
    def test_search(self):
        self.assertEqual(180180, search([1], 1000), "p108 answer")
        self.assertEqual(2768774904222066200260800,search([1], 10**9),
                         "answer for 1 billion mentioned in p108 forum thread") 

class P110:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestP110)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return search([1], 4000000)

if __name__ == "__main__":
    mtools.run(P110())
