# compute the last 10 digits of '28433*(2**7830457)+1'
import time

def solve():
    i = 28433
    t = 1
    b = j = 2**1000
    while t < 7830:
        j = b*j
        t = t + 1
        s = str(j)
        if len(s) > 10:
            j = int(s[len(s)-10:])
    left = 2**457
    r = i*j*left+1
    s = str(r)
    return s[len(s)-10:]

def test():
    pass

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

