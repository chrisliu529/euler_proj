import time

gtab = {1:[1], 2:[1,2]}

def solve():
    return special_set_str(7)

def special_set_str(n):
    l = special_set(n)
    print l
    return conv_str(l)

def conv_str(l):
    s = [str(x) for x in l]
    return ''.join(s)

def special_set(n):    
    if gtab.has_key(n):
        return gtab[n]

    i = 3
    st = special_set(n-1)
    init_s = st + [st[len(st)-1]+1]
    print 'init for %d:%s' % (n, init_s)
    s = init_s
    q = [s]
    while not verify(s):
        q.remove(s)
        ns = next_status(s)
#        print ns
        for e in ns:
            if not e in q:
                q.append(e)
        s = q[0]
        print 'q=%s' % q

    if not gtab.has_key(n):
        gtab[n] = s
    return s

def next_status(s):
    d = {}
    pre_c = False
    c = s[0]
    for i in range(len(s)):
        c = s[i]
        if pre_c == c:
            continue
        pre_c = c
        sb = list(s)
        sb[i] = sb[i]+1
        sb.sort()
        key = conv_str(sb)
        if not d.has_key(key):
            d[key] = sb
    l = d.values()
    print '%s->%s' % (s, l)
    return l

def verify(s):
    print 'v(%s)' % s
    #check unique 1!=1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    #quick check sum 2!=1
    if s[0] + s[1] <= s[len(s)-1]:
        return False
    #2!=2
    vs = list(s)
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            sum = s[i] + s[j]
            if sum in vs:
                return False
            vs.append(sum)
    #2 < 3
    if (len(s) >= 5):
        if (s[0] + s[1]+ s[2]) <= (s[len(s)-1] + s[len(s)-2]):
            return False

    return True

def test():
    test_verify()
    assert special_set_str(3) == '234'
#    assert special_set_str(4) == '3567'
#    r = special_set_str(5)
#    assert r == '69111213'
#    assert special_set_str(6) == '111819202225'

def test_verify():
    assert not verify([1, 2, 3])
    assert not verify([2, 2, 3])
    assert verify([2, 3, 4])
    assert not verify([2, 3, 4, 5])
    assert not verify([20, 29, 31, 39, 41])

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

'''
The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}
It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

{20, 31, 38, 39, 40, 42, 45}
20313839404245
20+31=51>45 6
51+38=89 > (45+42)=87 2
89+39=128>(87+40)=127 1

19, 31, 38, 39, 40, 42, 44

{11, 17, 20, 22, 23, 24}
11 -> A={6, 9, 11, 12, 13} Sum(A)=51

'''
