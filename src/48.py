import time, mtools, math

def solve():
    sum = 0
    for i in range(1, 1001):
        sum = sum + i**i
    s = str(sum)
    return s[len(s)-10:]

def test():
    pass

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
