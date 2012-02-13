import time, mtools

def solve():
    l1 = [0]
    l2 = [1]
    rules = [
        [(0,4), (4,0)],
        [(0,6), (0,9), (6,0), (9,0)],
        [(1,6), (1,9), (6,1), (9,1)],
        [(2,5), (5,2)],
        [(3,6), (3,9), (6,3), (9,3)],
        [(4,6), (4,9), (6,4), (9,4)],
        [(1,8), (8,1)]
        ]
    d = search(l1, l2, rules, 0, {})
    return len(d)

def search(l1, l2, rules, layer, d):
    if layer == 7:
        insert_result(l1, l2, d)
        return d
    rule = rules[layer]
    l1b = list(l1)
    l2b = list(l2)
    for r in rule:
        if insert_rule(l1, l2, r):
            search(l1, l2, rules, layer+1, d)
            l1 = list(l1b)
            l2 = list(l2b)
    return d

def insert_rule(l1, l2, r):
    (a, b) = r
    if insert_elem(l1, a) and insert_elem(l2, b):
        return True
    return False

def insert_elem(l, e):
    i = 0
    while i < len(l):
        if l[i] == e:
            return True
        elif l[i] < e:
            i = i + 1
        else:
            if len(l) < 6:
                l.append(e)
                l.sort()
                return True
            else:
                return False
    if len(l) < 6:
        l.append(e)
        l.sort()
        return True
    return False

def insert_result(l1, l2, d):
    l1s = extend_list(l1, 6, 10)
    l2s = extend_list(l2, 6, 10)
    for li in l1s:
        for lj in l2s:
            k1, k2 = make_key(li, lj)
            if not d.has_key(k1) and not d.has_key(k2):
                d[k1] = True

def extend_list(l, sz, lim):
    if len(l) == sz:
        return [l]
    s = set(range(lim)) - set(l)
    n = sz - len(l)
    ls = mtools.comb(list(s), n)
    lr = []
    for le in ls:
        lt = l + le
        lt.sort()
        lr.append(list(lt))
    return lr

def make_key(li, lj):
    lis = [str(x) for x in li]
    ljs = [str(x) for x in lj]
    return ''.join(lis + ljs), ''.join(ljs + lis)

def test():
    assert [[0,1]] == extend_list([0,1], 2, 2)
    assert [[0,1]] == extend_list([0,1], 2, 3)
    assert [[0,1,2]] == extend_list([0,1], 3, 3)
    assert [[0,1,2], [0,1,3]] == extend_list([0,1], 3, 4)
    assert '012013','013012' == make_key([0,1,2], [0,1,3])

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
