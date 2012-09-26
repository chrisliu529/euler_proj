'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import time, math, mtools

def unique(s):
    l = [ord(x) for x in s]
    return len(set(l)) == len(l)

def solve():
    l = [x for x in mtools.sieve_primes(10000) if len(str(x)) == 4]
    i = 0
    while i < len(l):
        s = set(l)
        lp = [int(x) for x in mtools.permute(list(str(l[i])))]
        si = set(lp) & s
        li = list(si)
        li.sort()
        for j in range(len(li)-2):
            for k in range(j+1,len(li)-1):
                d = li[k] - li[j]
                if (li[k]+d) in li:
                    if li[j] != 1487:
                        return str(li[j]) + str(li[k]) + str(li[k]+d)
        l = list(s - si)

def test():
    pass

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
