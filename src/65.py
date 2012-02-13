import math, time, mtools, sys

def solve():
    ec = e_convergent(33)
    l = mtools.separate_digits(ec)
    l = [int(x) for x in l]
    return sum(l)

def e_convergent(layer):
    s = 2
    l = [[1, 2*i, 1] for i in range(1, layer+1)]
    l = sum(l, [])
    l.reverse()
    con = None
    for x in l:
        if not con:
            con = (1, x)
        else:
            (b, a) = con
            con = (a, a*x+b)
    (b, a) = con
    return s*a + b

def test():
    assert e_convergent(1) == 11
    assert e_convergent(2) == 106

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

