'''
Created on 2012-8-27

@author: chrisliu
'''

import unittest
import time
import mtools

def build_arr(M, N):
    pm = mtools.sieve_primes(M+1)
    res = []
    for p in pm:
        v = 1
        l = []
        while v <= N:
            l.append(v)
            v *=p 
        res.append(l[:])
    return res

def hamming(M, N):
    arr = build_arr(M, N)
    return dfs(1, 0, arr, N)

def dfs(v, cur, arr, N):
    cnt = 0
    if cur == len(arr):
        if v<=N:
            return 1
        return 0
    if v > N:
        return 0
    for b in arr[cur]:
        vb = v
        v *= b
        c = dfs(v, cur+1, arr, N)
        if c > 0:
            cnt += c
        elif v > 1:
            return cnt #trim branch    
        v = vb
    return cnt

def no_prime_larger(m, n):
    i = 2
    while (n > 1) and (i*i <= n):
        while (n%i == 0):
            if i > m:
                return False
            n /= i
        i += 1
    if n <= m:
        return True
    return False

def direct_search(n, upper):
    i = 2
    cnt = 1 # 1 is hamming number
    while i <= upper:
        if no_prime_larger(n, i):
            cnt += 1
        i += 1
    return cnt

def solve():
    return hamming(100, 10**9)

class TP(unittest.TestCase):
    def test_direct_search(self):
        self.assertEqual(4, direct_search(2, 10))
        self.assertEqual(7, direct_search(3, 10))
        self.assertEqual(9, direct_search(5, 10))        

    def test_no_prime_larger(self):
        self.assertTrue(no_prime_larger(5, 10))
        self.assertFalse(no_prime_larger(5, 11))
        
    def test_hamming(self):
        self.assertEqual(direct_search(5, 10), hamming(5, 10))
        self.assertEqual(1105, hamming(5, 10**8))
        
    def test_build_arr(self):
        self.assertEqual([[1,2,4]], build_arr(2, 5))
        self.assertEqual([[1,2,4],[1,3],[1,5]], build_arr(5, 5))

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
