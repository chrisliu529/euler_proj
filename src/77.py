import math, time, mtools, sys

def solve():
    for i in range(50, 100):
        if sum_prime_ways(i) > 5000:
            return i

def sum_prime_ways(n):
    l = mtools.sieve_primes(n)
    l.reverse()
    ret = sum_prime_ways_rec(n, l, 0, {})
    #print 'sum_prime_ways(%d) = %d' % (n, ret)
    return ret

def sum_prime_ways_rec(n, l, p, tab):
    k = (n, p)
    if tab.has_key(k):
        return tab[k]
    if n == 1:
        return 0
    if l[p] == 2:
        if (n % 2) == 0:
            return 1
        else:
            return 0
    sum = 0
    for i in range(p, len(l)):
        r = n - l[i]
        if r == 0:
            sum = sum + 1
        elif r > 0:
            sum = sum + sum_prime_ways_rec(r, l, i, tab)
    tab[k] = sum
    #print 'sum_ways_rec(%s, %s, %s)=%d' % (n, l, p, sum)
    return sum

def test():
    assert 0 == sum_prime_ways(3)
    assert 1 == sum_prime_ways(4)
    assert 1 == sum_prime_ways(5)
    assert 5 == sum_prime_ways(10)
    assert 40899 == sum_prime_ways(100)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
