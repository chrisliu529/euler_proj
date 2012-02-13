import math, sys, time, mtools

def solve():
    max = 0
    for a in range(100):
        for b in range(100):
            c = a**b
            s = sum_digit(c)
            if s > max:
                max = s
    return max

def sum_digit(n):
    l = mtools.separate_digits(n)
    return sum(l)

def test():
    assert sum_digit(1) == 1
    assert sum_digit(21) == 3
    assert sum_digit(120) == 3
    assert sum_digit(100*100) == 1

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
