"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
from math import sqrt
import time

def is_prime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def prime(n):
    i = 2
    m = 3
    while i < n:
        m = m+2
        if is_prime(m):
            i = i + 1
    return m

def is_prime2(m,l):
    lim = sqrt(m)
    for i in l:
        if i > lim:
            return True
        if m % i == 0:
            return False
    return True

def prime2(n):
    m = 3
    l = []
    l.append(2)
    l.append(3)
    while len(l) < n:
        m = m+2
        if is_prime2(m,l):
            l.append(m)
    return m

"""
assert prime(4) == 7
assert prime(6) == 13
t = time.time()
print prime(10001)
print time.time() - t
"""

assert prime2(4) == 7
assert prime2(6) == 13
t = time.time()
print prime2(100001)
print time.time() - t
