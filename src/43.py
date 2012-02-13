import time, mtools

def test():
    assert divisible('1406357289')
    assert not divisible('140635728')

def divisible(n):
    primes = [2,3,5,7,11,13,17]
    for i in reversed(range(1,8)):
        if (int(n[i:i+3]) % primes[i-1]) != 0:
            return False
    return True

def solve():
    l = mtools.permute(list('1234567890'))
    l2 = [x for x in l if divisible(x)]
    l3 = [int(x) for x in l2]
    return sum(l3)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
