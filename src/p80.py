import math, time, mtools, sys

def solve():
    l = [i for i in range(2, 100)]
    l2 = [i*i for i in range(10)]
    s = set(l) - set(l2)
    sum = 0
    for i in s:
        sum = sum + sum_decimal_sqrt(i, 100)
    return sum

def test():
    assert try_div(400, 140) == 2
    assert try_div(66, 40) == 1
    assert try_div(11600, 1440) == 8
    assert try_div(1600, 14560) == 0
    assert try_div(700, 80) == 7
    assert try_div(9100, 940) == 9
    assert 1 == sum_decimal_sqrt(2, 1)
    assert 5 == sum_decimal_sqrt(2, 2)
    assert 12 == sum_decimal_sqrt(2, 5)
    v = sum_decimal_sqrt(2, 100)
    assert 475 == v
    assert 7 == sum_decimal_sqrt(5, 3)
    assert 20 == sum_decimal_sqrt(23, 3)

def sum_decimal_sqrt(i, n):
    int_part = int(math.sqrt(i))
    t = 1
    r = (i- int_part*int_part)*100
    d = int_part*20
    s = [int_part]
    while t < n:
        td = try_div(r, d)
        assert td >= 0 and td < 10
        #print 'try_div(%d,%d)=%d' % (r, d, td)
        s.append(td)
        r = (r - (d+td)*td)*100
        d = d*10 + td*20
        t = t + 1
    show_decimal(i, s)
    assert len(s) == n
    return sum(s)

def show_decimal(i, s):
    s2 = [str(x) for x in s]
    s3 = ''.join(s2)
    print 'sqrt(%d)=%s.%s' % (i, s3[0], s3[1:])

def try_div(r, d):
    dv = r/d
    if dv == 0:
        return 0
    while dv > 0:
        if r/(d+dv) == dv:
            return dv
        dv2 = dv - 1
        if (d+dv)*dv > r and (d+dv2)*dv2 <= r:
            return dv2
        dv = dv2
    return 0

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

