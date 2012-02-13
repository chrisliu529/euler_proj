'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, 
and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import time, math, mtools

def solve():
    return max_sum_primes(1000000)

def max_sum_primes(n):
    l = mtools.sieve_primes(n)
    lim = len(l)
    sum_max = l[lim-1]
    all_max = 0
    s_all_max = 0
    for i in range(lim-2):
        s_max = max = 0
        np = 2
        sum = l[i] + l[i+1]
#        print 'i=%s' % i
        j = i + 2
        no_add = True
        while j < lim:
            while (j < lim) and (np <= all_max) and (sum <= sum_max):
                sum = sum + l[j]
                j = j + 1
                np = np + 1
            if (sum > sum_max) or (j > lim):
                if no_add:
                    return s_all_max
                break
            if mtools.is_prime(sum):
                max = np
                s_max = sum
#                print 'max=%s s_max=%s' % (max, s_max)
            sum = sum + l[j]
            j = j + 1
            np = np + 1
            no_add = False
        if max > all_max:
            all_max = max
            s_all_max = s_max
#            print all_max, s_all_max
    return s_all_max

def test():
    assert 41 == max_sum_primes(100)
    assert 953 == max_sum_primes(1000)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
