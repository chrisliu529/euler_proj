'''
Created on 2012-3-4

@author: EvieChris
'''
import mtools

def get_max(l, i):
    if (i == 1):
        return 0
    return sum(l[-(i-1):])

def is_special_set(l):
    l.sort()
    tab = {}
    i = 1
    while i < len(l):
        m = get_max(l, i) 
        for subs in mtools.comb(l, i):
            s = sum(subs)
            if s <= m:
                return False
            try:
                if tab[s]:
                    return False
            except KeyError:
                tab[s] = i
        i += 1
    return True

def conv_set(l):
    return [int(x) for x in l.split(',')]

class q105:  
    def test(self):
        assert [37,48,34,59,39,41,40] == conv_set("37,48,34,59,39,41,40")
        assert not is_special_set([1,2,3])
        assert not is_special_set([1,2,3,4])
        assert is_special_set([2, 3, 4])
        assert is_special_set([3, 5, 6, 7])
        assert is_special_set([6, 9, 11, 12, 13])
        assert not is_special_set([81, 88, 75, 42, 87, 84, 86, 65])
        assert is_special_set([157, 150, 164, 119, 79, 159, 161, 139, 158])

    def solve(self):
        f = file("105_sets.txt")
        n = 0
        for l in f:
            s = conv_set(l)
            if is_special_set(s):
                n += sum(s) 
        f.close()
        return n

if __name__ == "__main__":
    mtools.run(q105())
