import math, time, mtools, sys

f_tab = {}

def solve():
    max = 1500000
    maxi = maxj = 0
    for i in range(1, 100):
        for j in range(1, 100):
            t = f(i, j)
            if t < 2000000 and t > max:
                max = t
                maxi = i
                maxj = j
            elif t > 2000000:
                break
    print (max, maxi, maxj)
    return maxi*maxj

def f(m, n):
    if m < n:
        return fr(n, m)
    return fr(m, n)

def fr(m, n):
    global f_tab
    if f_tab.has_key((m,n)):
        return f_tab[(m, n)]
    if m == 1 and n == 1:
        return 1
    if m > n:
        r = fr(m-1, n) + m*s(n)
        f_tab[(m, n)] = r
        return r
    r = fr(m, n-1) + n*s(m)
    f_tab[(m, n)] = r
    return r

def s(n):
    return sum(range(n+1))

def test():
    assert f(1, 1) == 1
    assert f(1, 2) == 3
    assert f(2, 2) == 9
    assert f(3, 2) == 18

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
