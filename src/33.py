import time

def solve():
    l = []
    for num in range(12, 97):
        for den in range(num+1, 99):
            if is_non_trivial(num, den):
                l.append((num, den))
    nmul = dmul = 1
    for (num, den) in l:
        nmul = nmul * num
        dmul = dmul * den
    assert 4 == len(l)
    return dmul/nmul

def is_non_trivial(n, d):
    if n%10 == d/10:
        n1 = n/10
        d1 = d%10
        if (n*d1 == d*n1):
            return True
    return False

def test():
    assert is_non_trivial(49, 98)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
