import time
from mtools import factors

def d(n):
    return sum(factors(n)) - n

def sum_amicable_pairs(lim):
    sum = 0
    for i in range(1,lim):
        j = d(i)
        if (i != j) and (d(j) == i):
                #print "(%d,%d)" % (i,j)
                sum = sum + i + j
    return sum/2

def solve():
    return sum_amicable_pairs(10000)

def test():
    assert d(220) == 284
    assert d(284) == 220

if __name__ == "__main__":
    test()
    t = time.time()
    print solve()
    print "(%s)" % (time.time() - t)
