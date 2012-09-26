import math, time, mtools, sys

def solve():
    return sum_ways(100)

def sum_ways(n):
    l = range(1, n)
    l.reverse()
    ret = sum_ways_rec(n, l, 0, {})
    return ret

def sum_ways_rec(n, l, p, tab):
    k = (n, p)
    if tab.has_key(k):
        return tab[k]
    if l[p] == 1:
        return 1
    sum = 0
    for i in range(p, len(l)):
        r = n - l[i]
        if r == 0:
            sum = sum + 1
        elif r > 0:
            sum = sum + sum_ways_rec(r, l, i, tab)
    tab[k] = sum
    #print 'sum_ways_rec(%s, %s, %s)=%d' % (n, l, p, sum)
    return sum

def test():
    assert 1 == sum_ways(2)
    assert 2 == sum_ways(3)
    assert 6 == sum_ways(5)
    #assert 4 == sum_ways(4)


if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
