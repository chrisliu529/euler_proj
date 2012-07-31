'''
Created on 2012-7-29

@author: EvieChris
'''

import mtools
import unittest

ref = {1: 0, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 3, 9: 4, 10: 4, 11: 5, 12: 4, 13: 5, 14: 5, 15: 5, 16: 4, 17: 5, 18: 5, 19: 6, 20: 5, 21: 6, 22: 6, 23: 6, 24: 5, 25: 6, 26: 6, 27: 6, 28: 6, 29: 7, 30: 6, 31: 7, 32: 5, 33: 6, 34: 6, 35: 7, 36: 6, 37: 7, 38: 7, 39: 7, 40: 6, 41: 7, 42: 7, 43: 7, 44: 7, 45: 7, 46: 7, 47: 8, 48: 6, 49: 7, 50: 7, 51: 7, 52: 7, 53: 8, 54: 7, 55: 8, 56: 7, 57: 8, 58: 8, 59: 8, 60: 7, 61: 8, 62: 8, 63: 8, 64: 6, 65: 7, 66: 7, 67: 8, 68: 7, 69: 8, 70: 8, 71: 9, 72: 7, 73: 8, 74: 8, 75: 8, 76: 8, 77: 8, 78: 8, 79: 9, 80: 7, 81: 8, 82: 8, 83: 8, 84: 8, 85: 8, 86: 8, 87: 9, 88: 8, 89: 9, 90: 8, 91: 9, 92: 8, 93: 9, 94: 9, 95: 9, 96: 7, 97: 8, 98: 8, 99: 8, 100: 8, 101: 9, 102: 8, 103: 9, 104: 8, 105: 9, 106: 9, 107: 9, 108: 8, 109: 9, 110: 9, 111: 9, 112: 8, 113: 9, 114: 9, 115: 9, 116: 9, 117: 9, 118: 9, 119: 9, 120: 8, 121: 9, 122: 9, 123: 9, 124: 9, 125: 9, 126: 9, 127: 10, 128: 7, 129: 8, 130: 8, 131: 9, 132: 8, 133: 9, 134: 9, 135: 9, 136: 8, 137: 9, 138: 9, 139: 10, 140: 9, 141: 10, 142: 10, 143: 10, 144: 8, 145: 9, 146: 9, 147: 9, 148: 9, 149: 9, 150: 9, 151: 10, 152: 9, 153: 9, 154: 9, 155: 10, 156: 9, 157: 10, 158: 10, 159: 10, 160: 8, 161: 9, 162: 9, 163: 9, 164: 9, 165: 9, 166: 9, 167: 10, 168: 9, 169: 10, 170: 9, 171: 10, 172: 9, 173: 10, 174: 10, 175: 10, 176: 9, 177: 10, 178: 10, 179: 10, 180: 9, 181: 10, 182: 10, 183: 10, 184: 9, 185: 10, 186: 10, 187: 10, 188: 10, 189: 10, 190: 10, 192: 8, 193: 9, 194: 9, 195: 9, 196: 9, 197: 10, 198: 9, 199: 10, 200: 9}

def hashable(l):
    l.sort()
    return ','.join([str(x) for x in l])

def check_list():
    d = {}
    for i in range(2, 201):
        d[i] = i
    return d

def verify(M):
    for k in ref:
        if ref[k] != M[k]:
            print "m(%s)=%s not %s" % (k, ref[k], M[k])
            return False
    return True

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
                try:
                    if M[e] >= 0:
                        continue
                except KeyError:
                    v = len(S)
                    M[e] = v
                    print e,v,S
                    print M
                    del cl[e]
                    if not cl:
                        if verify(M):
                            return sum(M.values())
                        return "error"

                S1 = S[:]
                S1.append(e)
                h = hashable(S1)
                try:
                    if visited[h]:
                        continue
                except KeyError:
                    visited[h] = True
                Q.append(S1)


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
