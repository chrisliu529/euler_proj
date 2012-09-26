import mtools, time

def solve():
    cnt = 0
    tab = build_tab()
    for i in range(1, 10000000):
        if eventual(i, tab) == 89:
            cnt = cnt + 1
    return cnt

def build_tab():
    d = {}
    for i in range(1, 568): #7*9*9
        d[i] = eventual_calc(i)
    return d

def eventual_calc(i):
    while True:
        l = mtools.separate_digits(i)
        i = sum([x*x for x in l])
        if i == 1 or i == 89:
            return i

def eventual(i, tab):
    if tab.has_key(i):
        return tab[i]
    l = mtools.separate_digits(i)
    i = sum([x*x for x in l])
    return tab[i]

def test():
    assert 1 == eventual_calc(44)
    assert 89 == eventual_calc(85)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
