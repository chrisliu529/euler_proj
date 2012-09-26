import time, mtools

def count_circular_primes(n):
    l = mtools.sieve_primes(n)
    count = 0
    for i in l:
        if is_circular(i, l):
            count = count + 1
    return count

def test():
    l = mtools.sieve_primes(1000)
    assert is_circular(197, l)
    assert 13 == count_circular_primes(100)

def is_circular(n, l):
    digits_num = len(str(n))
    p = 10**(digits_num-1)
    for i in range(0, digits_num):
        r = n % 10
        n = n / 10
        n = n + p*r
        if not mtools.is_prime(n):
            return False
    return True

def solve():
    return count_circular_primes(1000000)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
