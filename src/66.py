import math, time, mtools, sys

def solve():
    l = []
    unable = []
    for d in range(2, 1001):
        if is_square(d):
            continue
        x, y = pell(d)
        assert x*x - d*y*y == 1
        #print '%d: (%d,%d)' % (d, x, y)
        l.append((x,d))
    l.sort(reverse=True)
    print l[0]
    return l[0][1]

def get_fraction_list(n):
    q = m = int(math.sqrt(n))
    d = n - m*m
    p = (2*m)/d
    r = p*d - m
    l = [q]
    while p != 2*q:
        l.append(p)
        m = r
        assert (n - m*m) % d == 0
        d = (n - m*m)/d
        p = (q + m)/d
        r = p*d - m
    if len(l) % 2 == 0:
        #the period length is even
        return l
    # the period length is odd
    la = l[1:]
    return l + [p] + la

def convergent(l):
    s = l[0]
    l = l[1:]
    l.reverse()
    con = None
    for x in l:
        if not con:
            con = (1, x)
        else:
            (b, a) = con
            con = (a, a*x+b)
    (b, a) = con
    return s*a + b, a

def pell(d):
    l = get_fraction_list(d)
    assert len(l) > 1
    return convergent(l)

def is_square(n):
    i = int(math.sqrt(n))
    if i*i == n:
        return True
    return False

def test():
    assert is_square(4)
    assert not is_square(8)
    assert get_fraction_list(2) == [1, 2]
    assert get_fraction_list(3) == [1, 1]
    assert get_fraction_list(13) == [3,1,1,1,1,6,1,1,1,1]

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
