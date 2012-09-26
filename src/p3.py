"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

def max_prime_factor(n):
    start = 2
    m = find_prime_factor(start,n)
    while m != 0:
        n = n / m
        start = m
        m = find_prime_factor(start,n)
    return n

def find_prime_factor(start,n):
    for i in range(start,int(sqrt(n))):
        if n % i == 0:
            return i
    return 0

print max_prime_factor(600851475143)
