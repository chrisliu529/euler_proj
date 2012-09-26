import math, time, mtools

def solve():
    n = 1
    pn = 0
    i = 3
    while True:
        n = n + 4
        d = i - 1
        s = i*i
        for j in range(1,4):
            if mtools.is_prime(s-j*d):
                pn = pn + 1
        if n > 10*pn:
            return i
#        print i, n, pn
        i = i + 2
    return i

def test():
    pass

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
