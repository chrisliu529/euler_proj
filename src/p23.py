import time
from mtools import sum_of_divisors

upper_limit = 28123
abundant_tab = {}

def d(n):
    return sum_of_divisors(n) - n

def is_abundant(n):
    global abundant_tab
    if abundant_tab.has_key(n):
        return abundant_tab[n]
    v = (d(n) > n)
    abundant_tab[n] = v
    return v

def abundant_separatable(n):
    if n < 24:
        return False
    for i in range(12, n/2+1):
        if is_abundant(i) and is_abundant(n-i):
            return True
    return False

def solve():
    sum = 0
    for i in range(1,upper_limit+1):
        if not abundant_separatable(i):
            sum = sum + i
    return sum

def test():
    assert d(12) == 16
    assert is_abundant(12)
    assert abundant_separatable(24)

if __name__ == "__main__":
    test()
    t = time.time()
    print solve()
    print "(%s)" % (time.time() - t)
