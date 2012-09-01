import math, sys, time
import unittest

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

def count_digits(n):
    cnt = 0
    while n > 0:
        n = n / 10
        cnt += 1
    return cnt

def separate_digits(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n / 10
    l.reverse()
    return l

def combine_digits(l):
    l2 = list(l)
    l2.reverse()
    n = 0
    i = 0
    for x in l2:
        n += x*(10**i)
        i += 1
    return n

def comb(items, n=None):
    if n is None:
        n = len(items)
    if n == 0:
        yield []
    if n < 0:
        return   
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

def swap(l, i, j):
    t = l[i]
    l[i] = l[j]
    l[j] = t

def next_perm(items):
    n = len(items)
    i = n - 1
    while i > 0 and items[i-1] >= items[i]:
        i -= 1
    if i == 0:
        return []
    j = i - 1
    while i < n and items[i] > items[j] :
        i += 1;
    assert i <= n
    i -= 1
    swap(items, j, i);
    j += 1
    k = n-1
    while (j < k):
        swap(items, j, k);
        j += 1
        k -= 1
    return items

def dict_perm(items):
    nextp = items
    while nextp:
        yield nextp
        nextp = next_perm(nextp)

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

#P(n,m)=n(n-1)(n-2)...(n-m+1)= n!/(n-m)!
def p(n, m):
    return mul(range(n-m+1, n+1))

#C(n,m)=P(n,m)/m!
def c(n, m):
    if m > n:
        return 0
    if m > n/2:
        return c(n, n-m)
    return p(n, m)/fac(m)

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

def reverse_int(n):
    s = str(n)
    return int(reverse_str(s))

def reverse_str(s):
    rs = ''
    l = list(s)
    l.reverse()
    for x in l:
        rs = rs + x
    return rs

def is_palindrome(n):
    return n == reverse_int(n)

def unique(l):
    return list(set(l))
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

def is_square(t):
    r = int(math.sqrt(t))
    return r*r == t

class TestMtools(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_factors(self):
        self.assertEqual([1], factors(1))
        self.assertEqual([1, 2], factors(2))
        self.assertEqual([1, 3], factors(3))
        self.assertEqual([1,2,3,6], sort_factors(6))
        self.assertEqual([1,2,4,7,14,28], sort_factors(28))

    def test_separate_digits(self):
        self.assertEqual(separate_digits(101), [1, 0, 1])
        self.assertEqual(separate_digits(0), [])
        self.assertEqual(separate_digits(1041), [1, 0, 4, 1])
        self.assertEqual(separate_digits(10123456789012), [1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
    
    def test_combine_digits(self):
        self.assertEqual(combine_digits([]), 0)
        self.assertEqual(combine_digits([1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]), 10123456789012)
    
    def test_next_perm(self):
        self.assertEqual(separate_digits(839651247), next_perm(separate_digits(839647521)))
        self.assertEqual([1,0,1,1], next_perm([0,1,1,1]))
        self.assertEqual([1,1,2,1], next_perm([1,1,1,2]))
        self.assertEqual([1,2,1,1], next_perm([1,1,2,1]))
    
    def test_dict_perm(self):
        results = [[0,1,1,1], [1,0,1,1], [1,1,0,1], [1,1,1,0]]
        i = 0
        for n in dict_perm([0, 1, 1, 1]):
            self.assertEqual(results[i], n)
            i += 1
            
    def test_is_int_sqrt(self):
        self.assertTrue(is_square(4))
        self.assertFalse(is_square(3))
        self.assertTrue(is_square(17951*17951))
        self.assertFalse(is_square(17951*17950))
        self.assertTrue(is_square(1795123456789*1795123456789), "large number")
        self.assertFalse(is_square(1795123456789*1795123456788), "large number")
        
    def test_count_digits(self):
        self.assertEqual(1, count_digits(1))
        self.assertEqual(2, count_digits(10))
        self.assertEqual(9, count_digits(123456789))
        
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(22))
        self.assertTrue(is_palindrome(595))
        self.assertFalse(is_palindrome(122))
        
    def test_unique(self):
        self.assertEqual([1,2], unique([1,1,2,2]))
        self.assertEqual([1,2,3], unique([1,2,3]))
        self.assertEqual([], unique([]))
        
    def test_c(self):
        self.assertEqual(4, c(4,1))
        self.assertEqual(6, c(4,2))
        self.assertEqual(1, c(4,0))
        self.assertEqual(1, c(4,4))
        self.assertEqual(0, c(4,5))
        self.assertEqual(1, c(0,0))

    def test_comb(self):
        for a in comb([1,2],2):
            self.assertEqual([1,2], a)
        l = [a for a in comb([1,2],1)]
        self.assertEqual(2, len(l))
        self.assertEqual([1], l[0])
        self.assertEqual([2], l[1])
        l = [a for a in comb([1,2],0)]
        self.assertEqual(1, len(l))
        self.assertEqual([], l[0])
        l = [a for a in comb([1,2,3],2)]
        self.assertEqual(3, len(l))
        self.assertEqual([1,2], l[0])
        self.assertEqual([1,3], l[1])
        self.assertEqual([2,3], l[2])
        l = [a for a in comb([1,2,3],-1)]
        self.assertEqual(0, len(l))
        
    def test_sieve_primes(self):
        self.assertEqual([2,3], sieve_primes(5))
        self.assertEqual([2,3,5], sieve_primes(6))

def run(q):
    if q.test():
        t = time.time()
        print "answer = %s" % (q.solve())
        print "(%s)" % (time.time() - t)
