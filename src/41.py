'''
We shall say that an n-digit number is pandigital 
if it makes use of all the digits 1 to n exactly once. 

For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import time, mtools

def separate_ones(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n / 10
    return l

def pandigital(n):
    l = separate_ones(n)
    l.sort()
    return l == range(1, len(l)+1)

def solve():
    # guess upper limit
    l = mtools.sieve_primes(10000000)
    l = [x for x in l if pandigital(x)]
    return l[len(l)-1]

def test():
    assert pandigital(1234)
    assert not pandigital(234)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
