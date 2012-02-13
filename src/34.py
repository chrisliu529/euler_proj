'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import time, mtools

tab = [mtools.fac(x) for x in range(0, 10)]

def is_curious(n):
    global tab
    l = get_digits(n)
    l2 = [tab[x] for x in l]
    return n == sum(l2)

def get_digits(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n /10
    l.reverse()
    return l

def test():
    assert [1, 2, 3] == get_digits(123)
    assert is_curious(145)

def solve():
    l = []
    # upper limit guessed
    for i in range(10,100000):
        if is_curious(i):
            l.append(i)
    return sum(l)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
