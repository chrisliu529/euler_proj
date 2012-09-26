import math, time, mtools, sys

tab = {}

def solve():
    return three_to_two(10000)

def test():
    assert three_to_two(7) == 2
    assert three_to_two(8) == 3

def three_to_two(m):
    cnt = 0
    for d in range(3, m+1):
        down = d/3 + 1
        if d % 2 == 0:
            up = d/2
        else:
            up = d/2 + 1
        for n in range(down,up):
            if mtools.gcd(n, d) == 1:
                cnt = cnt + 1
    return cnt

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
