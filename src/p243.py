'''
Created on 2012-9-18

@author: chrisliu
'''

import mtools
import unittest
import time

primes = mtools.sieve_primes(100)

def get_n(l):
    l2 = [primes[i]**x for (i, x) in enumerate(l)]
    return mtools.mul(l2)    

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

def search(l, (m, n)):
    states = [l]
    visited = {}
    nm = 0
    dm = em = 1
    while True:
        s = states.pop(0)
        h = hashable(s)
        try:
            if visited[h]:
                continue
        except KeyError:
            visited[h] = True
        ps = [primes[i] for i in range(len(s))]
        pm = mtools.mul(ps)
        pm1 = mtools.mul([p-1 for p in ps])
        d = get_n(s)
        e1, d1 = normalize(d*pm1, (d-1)*pm)
        if e1*n < d1*m:
            return d
        if e1*dm < d1*em:
            em = e1
            dm = d1
            nm = d
        elif d > nm:
            continue
        states += expand_states(s)
        states.sort(cmp = lambda x,y: cmp(get_n(x), get_n(y)))

def normalize(e, d):
    g = mtools.gcd(e, d)
    return e/g, d/g  

def min_d(m, n):
    return search([1,1], (m, n))
    
def solve():
    return min_d(15499,94744)

class TP(unittest.TestCase):
    def test_min_d(self):
        self.assertEqual(12, min_d(2,5))

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
