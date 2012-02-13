import math, time, mtools, sys

def tri(n):
    return n*(n+1)/2

def sq(n):
    return n*n

def pent(n):
    return n*(3*n-1)/2

def hex(n):
    return n*(2*n-1)

def hep(n):
    return n*(5*n-3)/2

def oct(n):
    return n*(3*n-2)

def de_tri(n):
    return (int(math.sqrt(1+8*n))-1)/2

def de_sq(n):
    return int(math.sqrt(n))

def de_pent(n):
    return (int(math.sqrt(1+24*n))+1)/6

def de_hex(n):
    return (int(math.sqrt(1+8*n))+1)/4

def de_hep(n):
    return (int(math.sqrt(9+40*n))+3)/10

def de_oct(n):
    return (int(math.sqrt(4+12*n))+2)/6

def gen_nl(lim):
    fl = [(tri, 200), (sq, 100), (pent, 100), (hex,100), (hep, 100), (oct, 100)]
    nl = []
    for i in range(lim):
        (f, n) = fl[i]
        l = [f(x) for x in range(n)]
        l2 = [x for x in l if len(str(x)) == 4]
        nl.append(l2)
    return nl

def solve():
    return sum_cylic_list(6)

def sum_cylic_list(n):
    cl = gen_find_cylic_list(n)
    print cl
    return sum(cl)

def gen_find_cylic_list(n):
    nls = mtools.perm(gen_nl(n))
    for nl in nls:
        cl = find_cylic_list(nl, nl[0], [])
        if cl:
            return cl

def shift_right(l, i):
    if i == 0:
        return l
    assert i < len(l)
    l2 = [None for j in range(len(l))]
    for k in range(len(l)):
        l2[(k+i)%len(l)] = l[k]
    return l2

def find_cylic_list(nl, subset, acc):
    #print "find_cylic_list %s %s" % (subset, acc)
    layer = len(acc)
    if layer < len(nl)-1:
        for x in subset:
            acc.append(x)
            l = nl[layer+1]
            new_subset = [e for e in l if is_cylic(x, e)]
            r = find_cylic_list(nl, new_subset, acc)
            if r:
                return r
            acc.pop()
    else:
        last_elem = int(str(acc[len(nl)-2])[2:] + str(acc[0])[:2])
        if last_elem in subset:
            acc.append(last_elem)
            assert len(acc) == len(nl)
            if unique_index(acc):
                return acc

def is_cylic(m, n):
    return tail(m) == head(n)

def tail(x):
    return str(x)[2:]

def head(x):
    return str(x)[:2]

def unique_index(l):
    defl = [de_tri, de_sq, de_pent, de_hex, de_hep, de_oct]
    il = [defl[i](l[i]) for i in range(len(l))]
    return len(il) == len(set(il))

def test():
    fl = [(tri, 200), (sq, 100), (pent, 100), (hex,100), (hep, 100), (oct, 100)]
    for (f,n) in fl:
        r = f(n)
        assert r >= 10000
    assert is_cylic(8128, 2882)
    assert is_cylic(2882, 8281)
    assert is_cylic(8281, 8128)

    fl = [(tri, 105), (sq, 40), (pent, 35), (hex,32), (hep, 31), (oct, 30)]
    l = [f(n) for (f, n) in fl]
    assert unique_index(l)

    assert shift_right([1,2], 1) == [2, 1]
    assert shift_right([1,2], 0) == [1, 2]
    assert shift_right([1,2, 3], 2) == [2, 3, 1]
    
    r = gen_find_cylic_list(3)
    assert [8128, 2882, 8281] == r

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

