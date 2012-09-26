from math import sqrt

def factors_count(n):
    c = 0
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            c = c + 2
            if (n == i*i):
                c = c - 1
    return c

"""
def prime_factors(n):
    primes = []
    counters = []
    i = 2
    while (n > 1) and (i*i <= n):
        if n % i == 0:
            primes.append(i)
            c = 0
            while (n%i == 0):
                c = c + 1
                n = n / i
            counters.append(c)
        i = i + 1
    if n > 1:
        primes.append(n)
        counters.append(1)
    return primes,counters

def factors_count(n):
    l,c = prime_factors(n)
    mul = 1
    for x in c:
        mul = mul*(x+1)
    return mul
"""

def test():
    test_factors_count()

def test_factors_count():
    assert factors_count(1) == 1
    assert factors_count(3) == 2
    assert factors_count(6) == 4

def triangle_over_divisors(n):
    i = 1
    while True:
        i = i + 1
        if (i%2 == 0):
            c = factors_count(i/2)*factors_count(i+1)
        else:
            c = factors_count(i)*factors_count((i+1)/2)
        if c >= n:
            return i*(i+1)/2

def main():
    print triangle_over_divisors(500)

if __name__ == "__main__":
    test()
    main()
