import math, time, mtools, sys

def solve():
    l = mtools.sieve_primes(10000)
    lp = []
    layer = 5
    return sum(find_comb_primes(lp, l, 0, len(l)-layer+1, layer))

def find_comb_primes(lp, l, begin, end, layer):
    #print "find_comb_primes %s %s %s %s" % (lp, begin, end, layer)
    if len(lp) == layer:
        return lp
    for i in range(begin, end):
        lp.append(l[i])
        if all_comb_primes(lp):
            r = find_comb_primes(lp, l, i+1, len(l)-layer+len(lp)+1, layer)
            if r:
                return r
        lp.pop()

def all_comb_primes(l):
    if len(l) == 1:
        return True
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            s1 = str(l[i])
            s2 = str(l[j])
            if not mtools.is_prime(int(s1+s2)):
                return False
            if not mtools.is_prime(int(s2+s1)):
                return False
    return True

def test():
    assert all_comb_primes([3, 7, 109, 673])

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

