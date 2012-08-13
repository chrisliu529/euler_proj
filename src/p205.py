'''
Created on 2012-8-12

@author: csee
'''

import mtools
import unittest
import random

def get_answer():
    peter = ptab(4, 9)
    colin = ptab(6, 6)
    s = 0
    for i in range(9, 37):
        s += peter[i]*sum([colin[j] for j in range(6, i)])
    t = (4**9)*(6**6)
    return float(s)/t

def ptab(n, m):
    return ptab_rec(n, m, {}, [])
    
def ptab_rec(n, m, tab, l):
    if m == 0:
        try:
            tab[sum(l)] += 1
        except KeyError:
            tab[sum(l)] = 1
        return
    for i in range(1, n+1):
        l.append(i)
        ptab_rec(n, m-1, tab, l)
        l.pop()
    return tab

def sum_tab(tab):
    return sum([tab[key] for key in tab.keys()])    

class TP(unittest.TestCase):        
    def test_ptab(self):
        self.assertEqual(4**9, sum_tab(ptab(4,9)))
        pass

class P:
    def test(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TP)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def solve(self):
        return get_answer()

if __name__ == "__main__":
    mtools.run(P())
