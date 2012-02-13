'''
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with 
denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit 
recurring cycle. It can be seen that 1/7 has a 6-digit 
recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest 
recurring cycle in its decimal fraction part.
'''

import time

def recurring_cycle(m, n):
    q = []
    r = {}
    i = 0
    while True:
        tq = m / n
        tr = m % n
        if tr == 0:
            return 0
        if r.has_key(tr):
            return i - r[tr]
        q.append(tq)
        r[tr] = i
        m = 10*m
        i = i + 1

def longest(lim):
    max_r = max = 0
    for i in range(2, lim):
        if lim % i == 0:
            continue
        r = recurring_cycle(1,i)
        if (r > max_r):
            max_r = r
            max = i
    return max

def test():
    assert 1 == recurring_cycle(1,9)
    assert 6 == recurring_cycle(1,7)
    assert 7 == longest(10)

def solve():
    return longest(1000)

if __name__ == "__main__":
    test()
    t = time.time()
    print solve()
    print "(%s)" % (time.time() - t)
