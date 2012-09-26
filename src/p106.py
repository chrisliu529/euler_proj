import mtools

def need_compare(s1, s2):
    if (set(s1) & set(s2)):
        return False
    n = len(s1)
    if s1[0] > s2[0]:
        for i in range(1, n):
            if s1[i] <= s2[i]:
                return True
    else:
        for i in range(1, n):
            if s1[i] >= s2[i]:
                return True
    return False

def to_compare(combs):
    n = len(combs)
    s = 0
    for i in range(n):
        for j in range(i+1, n):
            if need_compare(combs[i], combs[j]):
                #print 'cmp: %s & %s' % (combs[i], combs[j])
                s += 1
    return s

def sum_c(n):
    s = 0
    l = range(n)
    for i in range(2, n-1):
        combs = mtools.comb(l, i)
        combs2 = [c for c in combs]
        #print combs2
        s += to_compare(combs2)
    return s

class q106: 
    def test(self):
        assert need_compare([1, 4], [2, 3])
        assert not need_compare([1, 2], [3, 4])
        assert 1 == sum_c(4)
        assert 70 == sum_c(7)
        
    def solve(self):
        return sum_c(12)
    
if __name__ == "__main__":
    mtools.run(q106())
    