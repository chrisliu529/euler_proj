import math, time, mtools, sys

def solve():
    return count_odd_period(10000)

def count_odd_period(lim):
    cnt = 0
    for i in range(2, lim+1):
        l = get_fraction_list(i)
        if (len(l) % 2) != 0:
            cnt = cnt + 1
    return cnt

def get_fraction_list(n):
    q = m = int(math.sqrt(n))
    if m*m == n:
        # a square number, no fraction
        return []
    d = n - m*m
    p = (2*m)/d
    r = p*d - m
    tab = {}
    l = []
    while True:
        if not tab.has_key((p, r, d)):
            tab[(p, r, d)] = True
            l.append(p)
        else:
            return l
        m = r
        assert (n - m*m) % d == 0
        d = (n - m*m)/d
        p = (q + m)/d
        r = p*d - m

def test():
    assert get_fraction_list(2) == [2]
    assert get_fraction_list(3) == [1, 2]
    assert get_fraction_list(13) == [1,1,1,1,6]
    assert count_odd_period(13) == 4

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

