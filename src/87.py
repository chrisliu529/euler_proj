import math, time, mtools, sys

def solve():
    return sp_prime(50000000)

# max <= 50000000
def sp_prime(max):
    d = {}
    cnt = 0
    l = mtools.sieve_primes(7072)
    la = [x for x in l if x < 85]
    lb = [x for x in l if x < 400]
    for a in la:
        for b in lb:
            for c in l:
                v = a*a*a*a + b*b*b + c*c
                if v < max and not d.has_key(v):
                    d[v] = True
                    cnt = cnt + 1
                if v >= max:
                    break
    return cnt

def test():
    assert sp_prime(50) == 4

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
