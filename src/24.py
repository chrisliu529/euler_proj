'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of 
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import time,mtools

def facs(lim):
    l = []
    i = 1
    k = 1
    while k < lim:
        l.append(k)
        i = i + 1
        k = mtools.fac(i)
    l.append(k)
    return l

def solve():
    return nth_digits(1000000,10)

def to_string(l):
    s = ''
    for x in l:
        s = s + str(x)
    return s

def insert_nth(l, i, n):
    t = l[n]
    for j in reversed(range(i, n)):
        l[j+1] = l[j]
    l[i] = t
    return l

def nth_digits(n, m):
    return to_string(nth_digits_l(n, m))

def nth_digits_l(n, m):
    f = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    l = [i for i in range(0, m)]
    if (n == 1):
        return l
    n = n - 1
    for i in reversed(range(1,m)):
        t = n / f[i-1]
        cur = m - 1 - i
        if t > 0:
            l = insert_nth(l, cur, cur + t)
            n = n % f[i-1]
    return l

def test_insert_nth():
    assert [0,2,1] == insert_nth([2,1,0], 0, 2)
    assert [0,2,1] == insert_nth([0,1,2], 1, 2)

def test_nth_digits():
    assert "012" == nth_digits(1,3)
    assert "021" == nth_digits(2,3)
    assert "201" == nth_digits(5,3)
    assert "210" == nth_digits(6,3)

def test():
    test_insert_nth()
    test_nth_digits()

#print facs(1000000)
if __name__ == "__main__":
    test()
    t = time.time()
    print solve()
    print "(%s)" % (time.time() - t)
