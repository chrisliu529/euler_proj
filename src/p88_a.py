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
    assert [[2,2],[2,3],[3,3]] == select_p([2,3],[2,2],2)
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
    return r

def min_product_sum_with_start(k, start):
    i = start
    while True:
        if not mtools.is_prime(i):
            p, c = mtools.prime_factors(i)
            #i-k + len(factors) == sum(factors)
            if search_match(i, p, c, k):
                return i
        i = i + 1

def search_match(i, p, c, k):
    return search_match_rec(i, p, c, i-k+2, 0)

'''
i: the integer to be checked if it's the min sum product number
p, c: the prime factors of i
t: i - k + len(factors)
s: sum(factors)
'''
def search_match_rec(i, p, c, t, s):
    if s > t:
        return False

    max_len = sum(c)
    search_len = max_len / 2 + 1
    for n in range(1, search_len):
        pl = select_p(p, c, n)
        for x in pl:
            p0 = mtools.mul(x)
            p1 = i/p0
            s1 = s + p0 + p1
            if s1 == t:
                return True
            if s1 < t:
                return False

    for j in range(len(p)):
        if c[j] == 0:
            continue
        c[j] = c[j] - 1
        r = search_match_rec(i/p[j], p, c, t+1, s+p[j])
        if r == True:
            return r
        c[j] = c[j] + 1

def select_p(p, c, n):
    l = []
    for i in range(len(p)):
        if c[i] > n:
            l = l + [p[i]]*n
        else:
            l = l + [p[i]]*c[i]
    lc = mtools.comb(l, n)
    ret = unique_list(lc)
    return ret

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
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

