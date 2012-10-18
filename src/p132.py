'''
Created on 2012-10-15

@author: chrisliu
'''

import mtools
import unittest
import time

def parse_line(line):
    return [int(n) for n in line.split(',')]

def solve():
    fl = mtools.factors(10**9)
    fl.sort()
    fl2 = [f for f in fl if f <= 500]
    print len(fl2), fl2
    f = open('111.txt')
    ps = []
    for line in f:
        ps += parse_line(line)
    f.close()
    psu = mtools.unique(ps)
    psu.sort()
    print len(psu), psu[:40]
    return sum(psu[:40])

if __name__ == "__main__":
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)
