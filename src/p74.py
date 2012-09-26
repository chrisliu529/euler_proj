import math, time, mtools, sys

fac_tab = [mtools.fac(x) for x in range(10)]
chain_tab = {}

def solve():
    cnt = 0
    for i in range(1, 1000000):
        n = chain(i)
        chain_tab[i] = n
        if n == 60:
            cnt = cnt + 1
    return cnt

def sum_fac(n):
    l = mtools.separate_digits(n)
    l2 = [fac_tab[x] for x in l]
    return sum(l2)

def chain(i):
    c = 1
    d = {i:True}
    while True:
        v = sum_fac(i)
        if chain_tab.has_key(v):
            return c + chain_tab[v]
        if d.has_key(v):
            return c
        d[v] = True
        c = c + 1
        i = v

def test():
    assert sum_fac(363600) == 1454
    assert sum_fac(145) == 145
    assert 5 == chain(69)
    assert 1 == chain(145)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
