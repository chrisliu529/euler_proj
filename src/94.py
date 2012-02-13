import mtools, time, math

def solve():
    return sum_perimeter(333333333)

def sum_perimeter(lim):
    sum = 0
    k = 2
    while k <= lim:
        p = 3*k+1
        if check_more(k):
            sum = sum + p
        p = 3*k-1
        if check_less(k):
            sum = sum + p
        k = k + 1
        if k % 100000 == 0:
            #pass
            print k, sum
    return sum

#(k, k, k+1)
def check_more(k):
    r = perfect_square((3*k+1)*(k-1))
    if r > 0 and (r*(k+1) % 4) == 0:
        return True
    return False

#(k, k, k-1)
def check_less(k):
    r = perfect_square((3*k-1)*(k+1))
    if r > 0 and (r*(k-1) % 4) == 0:
        return True
    return False

def s(k):
    return math.sqrt((3*k+1)*(k-1))*(k+1)/4

def s2(k):
    return math.sqrt((3*k-1)*(k+1))*(k-1)/4

def perfect_square(n):
    r = int(math.sqrt(n))
    if r*r == n:
        return r
    return 0

def test():
    assert check_more(5)
    assert not check_more(4)
    assert not perfect_square(5)
    assert perfect_square(10**20)
    assert not perfect_square(10**20+1)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
