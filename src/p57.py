import math, time, mtools

def solve():
    return get_cnt(1000)

def get_cnt(lim):
    rn = 1
    d = 2
    cnt = 0
    for i in range(lim):
        n = rn + d
        d_digits = mtools.separate_digits(d)
        n_digits = mtools.separate_digits(n)
        if len(n_digits) > len(d_digits):
            cnt = cnt + 1
        tmp = rn
        rn = d
        d = 2*d + tmp
    return cnt

def test():
    assert get_cnt(8) == 1

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
