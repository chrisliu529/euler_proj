'''
Created on 2012-7-29

@author: EvieChris
'''

import mtools
import unittest

def hashable(l):
    l.sort()
    return ','.join([str(x) for x in l])

def check_list():
    d = {}
    for i in range(2, 201):
        d[i] = i
    return d

def get_answer():
    M = {}
    visited = {}
    M[1] = 0
    Q = []
    S = [1]
    cl = check_list()
    Q.append(S)
    while True:
        S = Q.pop(0)
        for x in S:
            for y in S:
                e = x+y
                if e in S or e > 200:
                    continue
                S1 = S[:]
                S1.append(e)
                h = hashable(S1)
                try:
                    if visited[h]:
                        continue
                except KeyError:
                    visited[h] = True
                Q.append(S1)
                try:
                    if M[e] >= 0:
                        continue
                except KeyError:
                    v = len(S)
                    M[e] = v
                    print e,v,S
                    del cl[e]
                    if cl:
                        continue
                    return sum(M.values())

class TP(unittest.TestCase):
    def test_m(self):
        pass

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
