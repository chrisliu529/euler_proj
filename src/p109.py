import mtools
from test.test_compiler import Toto

zones = range(1, 21) + [25]
tags = "SDT"

class Score:
    def __init__(self, v, t):
        self.value = v
        self.tag = t

    def __str__(self):
        return '(%s, %s)' % (self.value, self.tag)  
    
def init_points():
    dps = [Score(2*x, "D"+str(x)) for x in zones]
    ps = []
    for i in range(3):
        for z in zones:
            v = (i+1)*z
            if (v != 75): #no treble of bull
                s = Score(v, tags[i]+str(z))
                ps.append(s)
    ps.sort(cmp = lambda x,y: cmp(x.value, y.value))
    return dps, ps

def encode_way(l):
    if len(l) == 3 and l[2] > l[1]:
        t = l[2]
        l[2] = l[1]
        l[1] = t
    return ''.join(l)
    
class SearchContext:
    def __init__(self, cnt):
        self.count = cnt
        self.ways = {}
        self.steps = []
            
    def add_step(self, step):
        self.steps.append(step)
        
    def remove_step(self):
        self.steps.pop()
        
    def account_checkout(self):
        ew = encode_way(list(self.steps))
        try:
            if self.ways[ew]:
                return
        except KeyError:
            self.ways[ew] = True
            self.count += 1

def dart(n, i, sc):
    assert i == 1 or i == 2 or i == 3
    
    #allocate in reverse order
    #last dart must double
    if i == 1:
        for p in double_points:
            n1 = n
            n -= p.value
            step = p.tag
            if (n > 0):
                sc.add_step(step)
                dart(n, 2, sc)
                sc.remove_step()
            elif (n == 0):
                sc.add_step(step)
                sc.account_checkout()
                sc.remove_step()
            else:
                return
            n = n1
    elif i == 2:
        #free allocation
        for p in points:
            n1 = n
            n -= p.value
            step = p.tag
            if (n > 0):
                sc.add_step(step)
                dart(n, 3, sc)
                sc.remove_step()
            elif (n == 0):
                sc.add_step(step)
                sc.account_checkout()
                sc.remove_step()
            else:
                return
            n = n1            
    else:
        #done allocation
        for p in points:
            n1 = n
            n -= p.value
            step = p.tag
            if n == 0:
                sc.add_step(step)
                sc.account_checkout()
                sc.remove_step()
            if n < 0:
                return
            n = n1

def checkout(n):
    sc = SearchContext(0)
    dart(n, 1, sc)
    return sc.count

def total_checkout(m):
        l = [(n, checkout(n)) for n in range(1, m)]
        a = 0
        for (x, y) in l:
            if y > 0:
                a += y
        return a

class q109: 
    def test(self):
        assert 11 == checkout(6)
        assert 5 == checkout(5)
        assert 42336 == total_checkout(171)
        
    def solve(self):
        return total_checkout(100)

if __name__ == "__main__":
    double_points, points = init_points()
    mtools.run(q109())
