'''
Created on 2012-5-14

@author: csee
'''

import mtools

def possible_nums(n, d, i):
    nums = []
    base = [d]*(n-i)
    for j in range(10**i):
        l = base + mtools.separate_digits(j)
        if len(l) < n:
            l += [0]*(n-len(l))
        nums.append(l)
    return nums

def M(n, d):
    i = 1
    while i < n:
        pns = possible_nums(n, d, i)
        for ns in pns:
            ns.sort()
            for num in mtools.dict_perm(ns):
                if num[0] == 0:
                    continue
                inum = mtools.combine_digits(num)
                if mtools.is_prime(inum):
                    return n - i
        i += 1   

def N(n, d):
    i = 1
    prime_found = False
    cnt = 0
    checked ={}
    while i < n and not prime_found:
        pns = possible_nums(n, d, i)
        for ns in pns:
            ns.sort()
            for num in mtools.dict_perm(ns):
                if num[0] == 0:
                    continue
                inum = mtools.combine_digits(num)
                try:
                    if checked[inum]:
                        continue
                except KeyError:
                    checked[inum] = True
                if mtools.is_prime(inum):
                    prime_found = True
                    cnt += 1
        i += 1
    return cnt

def S(n, d):
    i = 1
    prime_found = False
    primes_sum = 0
    checked ={}
    while i < n and not prime_found:
        pns = possible_nums(n, d, i)
        for ns in pns:
            ns.sort()
            for num in mtools.dict_perm(ns):
                if num[0] == 0:
                    continue
                inum = mtools.combine_digits(num)
                try:
                    if checked[inum]:
                        continue
                except KeyError:
                    checked[inum] = True
                if mtools.is_prime(inum):
                    prime_found = True
                    primes_sum += inum
        i += 1
    return primes_sum

class p111: 
    def test(self):
        assert 3 == M(4, 1)
        assert 2 == M(4, 0)
        assert 3 == M(4, 7)
        assert 1 == N(4, 2)
        assert 12 == N(4, 3)
        assert 13 == N(4, 0)
        assert 67061 == S(4, 0)
        assert 22275 == S(4, 1)
        assert 2221 == S(4,2)
        
    def solve(self):
        return sum([S(10, d) for d in range(10)])

if __name__ == "__main__":
    mtools.run(p111())
