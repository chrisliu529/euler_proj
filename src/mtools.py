import math, sys, time

def phi(n):
    p, c = prime_factors(n)
    s = n
    for x in p:
        s = s - s/x
    return s

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def separate_digits(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n / 10
    l.reverse()
    return l

def comb(items, n=None):
    if n is None:
        n = len(items)    
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[i+1:]
            for c in comb(rest, n-1):
                yield v + c

def perm(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[:i] + items[i+1:]
            for p in perm(rest, n-1):
                yield v + p

def permute(seq):
    seqn = [seq.pop()]
    while seq:
        newseq = []
        new = seq.pop()
        for i in range(len(seqn)):
            item = seqn[i]
            for j in range(len(item)+1):
                newseq.append(''.join([item[:j],new,item[j:]]))
        seqn = newseq
    return  seqn

def mul(l):
    m = 1
    for x in l:
        m = m * x
    return m

def sieve_primes(n):
    l = [True for x in range(0,n)]
    lim = int(math.sqrt(n))+1
    for i in range(2,lim):
        if l[i]:
            for j in range(i+i,len(l),i):
                l[j] = False
    return [x for x in range(2,n) if l[x]]

def fac(n):
    assert n >= 0
    if n == 0 or n == 1:
        return 1
    mul = 1
    for i in range(2, n+1):
        mul = i * mul
    return mul

def sum_of_divisors(n):
    prod = 1
    k = 2
    while k*k <= n:
        p = 1
        while n % k == 0:
            p = p * k + 1
            n = n / k;
        prod = prod * p
        k = k + 1
    if n > 1:
        prod = prod * (1+n);
    return prod;

def factors_count(n):
    c = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            c = c + 2
            if (n == i*i):
                c = c - 1
    return c

def factors(n):
    l = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            l.append(i)
            if (n != i*i):
                l.append(n/i)
    return l

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

def factors_count2(n):
    l,c = prime_factors(n)
    mul = 1
    for x in c:
        mul = mul*(x+1)
    return mul

def is_prime2(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    if n < 0:
        n = abs(n)
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f = f + 6
    return True

def test_prime():
    L = [-5,2,3,5,7,97]
    for x in L:
        assert is_prime(x)

def test_prof_prime():
    t = time.time()
    L = [x for x in range(1,1000000) if is_prime(x)]
    t2 = time.time()
    L2 = [x for x in range(1,1000000) if is_prime2(x)]
    t3 = time.time()
    print "(%s, %s)" % (t2-t, t3-t2)

def sort_factors(n):
    l = factors(n)
    l.sort()
    return l

def test_factors():
    assert [1] == factors(1)
    assert [1,2] == factors(2)
    assert [1,3] == factors(3)
    assert [1,2,3,6] == sort_factors(6)
    assert [1,2,4,7,14,28] == sort_factors(28)

def test_separate_digits():
    assert separate_digits(101) == [1, 0, 1]
    assert separate_digits(0) == []
    assert separate_digits(1041) == [1, 0, 4,1]
    assert separate_digits(10123456789012) == [1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]

def test():
    test_prime()
    #test_prof_prime()
    test_factors()
    test_separate_digits()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "running test..."
        test()
        print "test passed."
    else:
        L = [is_prime(int(x)) for x in sys.argv[1:]]
        print L
