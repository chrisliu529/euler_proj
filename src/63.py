import math, time, mtools, sys

def test():
    pass

def solve():
    s = set()
    for a in range(1, 10):
        for b in range(1, 100):
            n = a**b
            if b == len(str(n)):
                print '%d**%d = %d' % (a, b, n)
                s.add(n)
    return len(s)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
