'''
Starting with the number 1 and moving to the right in a 
clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral 
formed in the same way?
'''

import time

def spiral_diag_sum(n):
    assert (n%2 == 1)
    if (n == 1):
        return 1
    sum = 1
    lim = (n+1)/2
    for i in range(1, lim):
        sum = sum + inc_value(i)
    return sum

def inc_value(n):
    #computed with p28.m
    return 16*n*n + 4*n + 4

def test():
    assert spiral_diag_sum(1) == 1
    assert spiral_diag_sum(3) == 25
    assert spiral_diag_sum(5) == 101

def solve():
    return spiral_diag_sum(1001)

if __name__ == "__main__":
    test()
    t = time.time()
    print solve()
    print "(%s)" % (time.time() - t)
