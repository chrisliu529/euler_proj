# coding=utf-8
'''
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for 
the consecutive values n = 0 to 39. However, when n = 40, 
402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n² − 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values n = 0 to 79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, 
for the quadratic expression that produces the maximum number of primes 
for consecutive values of n, starting with n = 0.
'''

import time, mtools

def quadratic(lim):
    l = [(x, y) for x in range(1-lim, lim) for y in range(x, lim)]
    n = 0
    while len(l) > 1:
        #print n,l
        l = filter_list(l, n)
        #print l
        n = n + 1
    assert len(l) == 1
    #print n
    (a, b) = l[0]
    print (a, b)
    return a*b

def form_prime(a, b, n):
    v = n*n + a*n + b
    if v < 0:
        v = abs(v)
    return mtools.is_prime(v)

def filter_list(l, n):
    for i in range(0, len(l)):
        (a, b) = l[i]
        if not form_prime(a, b, n):
            l[i] = 0
    return [x for x in l if x != 0]

def solve():
    return quadratic(1000)

if __name__ == "__main__":
    t = time.time()
    print solve()
    print "(%s)" % (time.time() - t)
