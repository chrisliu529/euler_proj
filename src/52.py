'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

import time, math, mtools

def solve():
    i = 1
    while True:
        i = i + 1
        s = str(i)
        if same_digits(s, 2*i) and same_digits(s, 3*i) and same_digits(s, 4*i) and same_digits(s, 5*i) and same_digits(s, 6*i):
            return s

def same_digits(s, n):
    l1 = list(s)
    l1.sort()
    l2 = list(str(n))
    l2.sort()
    return l1 == l2

def test():
    assert same_digits('125874', 251748)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

'''
md2perpe:
For this problem I didn't even use a computer. I just remembered that the repeating sequence of digits in the decimal representation of 1/7 has the desired property.

1/7 = 0.142857 142857 142857 ...

2 * 142857 = 285714
3 * 142857 = 428571
4 * 142857 = 571428
5 * 142857 = 714285
6 * 142857 = 857142
but
7 * 142857 = 999999 
'''
