import math, time, mtools, sys

M = 1000000

def solve():
    i = 1000
    j = 2000
    while True:
        m = (i+j)/2
        print m, i, j
        v = count_cuboid(m)
        if v <= M and count_cuboid(m+1) >= M:
            return m+1
        if v < M:
            i = m
            continue
        if v == M:
            return m+1
        if v > M:
            j = m

def test():
    assert is_perfect_square(4)
    assert is_perfect_square(25)
    assert separate(3, 4) == 2
    assert separate(6, 8) == 3
    assert separate(6, 9) == 2
    assert count_cuboid0(6) == 6
    assert count_cuboid(6) == 6
    assert count_cuboid(10) == count_cuboid0(10)
    assert count_cuboid(20) == count_cuboid0(20)
    assert count_cuboid(99) == 1975
    #assert count_cuboid(100) == 2060

def count_cuboid0(s):
    cnt = 0
    d = {}
    for a in range(1, s+1):
        for b in range(a, s+1):
            for c in range(b, s+1):
                a_b = a + b
                if is_perfect_square(c*c+a_b*a_b):
                    k = (c,a_b)
                    if d.has_key(k):
                        d[k] = d[k] + 1
                    else:
                        d[k] = 1
                    cnt = cnt + 1
    #print d
    #print 'count_cuboid(%d)=%d' % (s, cnt)
    return cnt

def count_cuboid(s):
    cnt = 0
    d = {}
    for m in range(1, s+1):
        for n in range(m+1, s+1):
            a = n*n - m*m
            if a > 2*s:
                break
            t = m*n
            if t > s:
                break
            b = 2*t
            #print a,t
            k = s / a
            for i in range(1, k+1):
                ta = i*a
                tb = i*b
                r = separate(ta, tb)
                if r > 0:
                    key = (ta, tb)
                    if not d.has_key(key):
                        cnt = cnt + r
                        d[key] = True
            if b <= s:
                k = s / b
                for i in range(1, k+1):
                    ta = i*a
                    tb = i*b
                    r = separate(tb, ta)
                    if r > 0:
                        key = (tb, ta)
                        if not d.has_key(key):
                            cnt = cnt + r
                            d[key] = True

    #print 'count_cuboid(%d)=%d' % (s, cnt)
    return cnt

# b = b1 + b2 (a >= b1 >= b2)
# count the number (b1,b2)
def separate_dbg(a, b):
    r = separate(a, b)
    if r > 0:
        print 'separate(%d,%d)=%d' % (a, b, r)
    return r

def separate(a, b):
    t = b/2
    if a >= b-1:
        return t
    if a > t:
        r = a-t
        if b % 2 == 0:
            r = r + 1
        return r
    return 0

def is_perfect_square(n):
    i = int(math.sqrt(n))
    return i*i == n

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
