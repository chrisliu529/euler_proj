import mtools, time

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return float(x)/y

def make_ops():
    l = []
    ops = [add, sub, mul, div]
    for i in ops:
        for j in ops:
            for k in ops:
                for o in ops:
                    l.append([i,j,k,o])
    return l

ops_list = make_ops()

def solve():
    m = 0
    le = mtools.comb(range(1,10), 4)
    for es in le:
        l = target_numbers(es)
        t = consecutive_numbers(l)
        #print es, t
        if t > m:
            m = t
            lr = list(es)
            lr.sort()
            print lr, t
    return lr

def target_numbers(es):
    d = {}
    nl = mtools.perm(es)
    for l in nl:
        for ops in ops_list:
            r = ops[0](l[0], l[1])
            r1 = ops[1](r, l[2])
            r1 = ops[2](r1, l[3])
            if r1 > 0:
                r1 = round_int(r1)
            if r1 > 0 and not d.has_key(r1):
                d[r1] = True
            #(a b) (c d)
            r2 = ops[2](l[2], l[3])
            r2 = ops[1](r, r2)
            if r2 > 0:
                r2 = round_int(r2)
            if r2 > 0 and not d.has_key(r2):
                d[r2] = True
    return d.keys()

def consecutive_numbers(l):
    li = make_int(l)
    i = 1
    while i in l:
        i = i + 1
    return i-1

def make_int(l):
    return [round_int(x) for x in l]

def round_int(x):
    if abs(x - int(x)) < 0.00001:
        return int(x)

    if abs(x - int(x) - 1) < 0.00001:
        return int(x) + 1
    
    return 0

def test():
    assert [1] == make_int([div(2,7) + div(5, 7)])
    l = target_numbers([1, 2, 3, 4])
    #print l
    assert 31 == len(l)
    assert 28 == consecutive_numbers(l)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
