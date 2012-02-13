import mtools, time, math

global_tab = {}

def solve():
    max = 0
    for i in range(12496, 1000000):
        l = amicable_chain(i)
        if max < len(l):
            max = len(l)
            emin = min(l)
    return [max, emin]

def amicable_chain(start):
    if start > 1000000:
        return []
    l = [start]
    s = start
    while True:
        next = chain_next(s)
        if next in l:
            return l[l.index(next):]
        if next > 1000000:
            return []
        l.append(next)
        s = next

def chain_next(s):
    if global_tab.has_key(s):
        return global_tab[s]
    r = mtools.sum_of_divisors(s) - s
    global_tab[s] = r
    return r

def test():
    assert  [220, 284] == amicable_chain(220)
    assert  [12496, 14288, 15472, 14536, 14264] == amicable_chain(12496)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

