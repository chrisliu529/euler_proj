import math, time, mtools, sys

def solve():
    return sum_min(12001)

def sum_min(border):
    s = 0
    d = {}
    r = 2
    for k in range(2, border):
        r = min_product_sum(k)
        if not d.has_key(r):
            d[r] = True
            s = s + r
    return s

def test():
    assert 4 == min_product_sum(2)
    assert 6 == min_product_sum(3)
    assert 8 == min_product_sum(4)
    assert 8 == min_product_sum(5)
    assert 12 == min_product_sum(6)
    assert 30 == sum_min(7)
    assert 16 == min_product_sum(10)
    assert 16 == min_product_sum(11)
    assert 16 == min_product_sum(12)
    assert 61 == sum_min(13)
    assert 48 == min_product_sum(35)
    assert 2061 == sum_min(100)

def min_product_sum(k):
    r = min_product_sum_with_start(k, k)
    #print 'min_product_sum(%d) = %d' % (k, r)
    return r

def min_product_sum_with_start(k, start):
    #print 'min_product_sum_with_start(%d,%d) = ' % (k, start),
    i = start
    while True:
        if not mtools.is_prime(i):
            p, c = mtools.prime_factors(i)
            #i-k + len(factors) == sum(factors)
            if search_match(i, p, c, k):
                #print i
                return i
        i = i + 1

def search_match(i, p, c, k):
    #print 'search_match(%s, %s, %s, %s)' % (i, p, c, k)
    return search_match_rec(i, p, c, i-k+2, 0)

'''
i: the integer to be checked if it's the min sum product number
p, c: the prime factors of i
t: i - k + len(factors)
s: sum(factors)
'''
def search_match_rec(i, p, c, t, s):
    #print 'search_match_rec(%s, %s, %s, %s, %s)' % (i, p, c, t, s)
    if s > t or i == 1:
        return False

    max_len = sum(c)
    search_len = max_len / 2 + 1
    for n in range(1, search_len):
        pl = select_p(p, c, n)
        #print i, t, pl
        for ps in pl:
            p0 = mul_p(p,ps)
            p1 = i/p0
            s1 = s + p0 + p1
            if s1 == t:
                return True
            if s1 < t:
                break
            remove_counter(c, ps)
            r = search_match_rec(p1, p, c, t+1, s+p0)
            if r == True:
                return r
            add_counter(c, ps)

def remove_counter(c, ps):
    for i in ps:
        c[i] = c[i] - 1

def add_counter(c, ps):
    for i in ps:
        c[i] = c[i] + 1

def select_p(p, c, n):
    l = []
    for i in range(len(p)):
        if c[i] > n:
            l = l + [i]*n
        elif c[i] > 0:
            l = l + [i]*c[i]
    lc = mtools.comb(l, n)
    lu = unique_list(lc)
    lu.sort(cmp=lambda x,y: cmp(mul_p(p, x), mul_p(p, y)))
    return lu

def mul_p(p, x):
    m = 1
    for i in x:
        m = m * p[i]
    return m

def unique_list(l):
    d = {}
    rl = []
    for x in l:
        t = tuple(x)
        if not d.has_key(t):
            d[t] = True
            rl.append(x)
    return rl

if __name__ == "__main__":
    test()
    print 'test passed!'
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

