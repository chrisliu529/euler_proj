import math, time, mtools, sys

def solve():
    i = 100
    d = {}
    while True:
        cs = cube_str(i)
        if d.has_key(cs):
            d[cs].add(i)
            if len(d[cs]) == 5:
                return smallest(d[cs])
        else:
            d[cs] = set([i])
        i = i + 1

def cube(n):
    return n*n*n

def cube_str(i):
    st = str(cube(i))
    l = [x for x in st]
    l.sort()
    return ''.join(l)

def smallest(s):
    l = list(s)
    m = min(l)
    return cube(m)

def test():
    assert cube_str(345) == '01234566'

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
