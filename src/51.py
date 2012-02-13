import time, math, mtools

def detect(n, l, l2):
    sl = [x for x in l if len(x) == n]
    l3 = make_couple(sl, l2)
    max = 0
    min_digit = 0
    digits = len(l2)
    if l2[0] == 0:
        s = 1
    else:
        s = 0
    max_list = []
    for k in range(s, 10**digits):
        dlist = [x for x in l3 if int(x[1]) == k]
        dlen = len(dlist)
        if dlen > max:
            max = dlen
            min_digit = dlist[0]
            max_list = dlist
    print max_list
    return max, combine(min_digit, l2)

def combine(d, l2):
    same_d, s = d
    l = ['d' for i in range(len(s)+len(l2))]
    for e in l2:
        l[e] = same_d
    j = 0
    for i in range(len(s)):
        while l[j] != 'd':
            j = j + 1
        l[j] = s[i]
    return ''.join(l)

def make_couple(l, dl):
    l2 = []
    for x in l:
        d, is_same = is_same_digits(x, dl)
        if is_same:
            l2.append((d, remove_digits(x, dl)))
    return l2

def remove_digits(x, l):
    lx = list(x)
    for i in l:
        lx[i] = 'd'
    lx = [e for e in lx if e != 'd']
    return ''.join(lx)

def is_same_digits(x, dl):
    d = x[dl[0]]
    for i in range(1, len(dl)):
        if d != x[dl[i]]:
            return d, False
    return d, True

def solve():
    l = [str(x) for x in mtools.sieve_primes(1000000)]
    for i in range(5,8):
        dls = mtools.comb(range(i-1), 3)
        for l2 in dls:
            l2.sort()
            print i, l2
            n, p = detect(i, l, l2)
            if n == 8:
                return p

def test_is_same_digits(d, l):
    d2, b = is_same_digits(d, l)
    return b

def test():
    assert test_is_same_digits('1112', range(3))
    assert not test_is_same_digits('1122', [1,2,3])
    assert test_is_same_digits('51112', [1,2,3])
    assert remove_digits('12345', range(1,4)) == '15'
    assert remove_digits('1234',range(3)) == '4'
    assert remove_digits('1234',range(2)) == '34'
    assert remove_digits('1204',range(2)) == '04'
    assert combine(('2', '13'), range(1,4)) == '12223'

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
