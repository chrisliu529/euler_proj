import time

def solve():
    hs1 = hs2 = ts1 = ts2 = '1'
    f1 = f2 = 1
    nb = n = 2
    tail = head = False
    lb = 1
#    while n < 2750:
    while not (tail and head):
        tail = head = False
#        f3 = f1 + f2
        hs3 = add_head(hs1, hs2)
        ts3 = add_tail(ts1, ts2)
        n = n + 1
        '''
        s = str(f3)
        if len(s) > lb:
            lb = len(s)
            print len(s), n-nb
            nb = n
        hs3r = s[:9]
        ts3r = s[len(s)-9:]
        print n, f3
        if len(s) > 9:
            print ts3r, ts3
            assert ts3r == ts3
        if len(s) > 20:
            print hs3r, hs3t
            assert hs3r == hs3t
            '''
        hs3t = hs3[:9]
        if is_pandigit(hs3t):
            print 'head "%s" %d' % (hs3, n)
            head = True
            if is_pandigit(ts3):
                print 'tail "%s" %d' % (ts3, n)
                tail = True
        hs1 = hs2
        hs2 = hs3
        ts1 = ts2
        ts2 = ts3
#        f1 = f2
#        f2 = f3

def add_head(hs1, hs2):
    if hs2[0] < hs1[0]:
        #one more digit appear
        hs1 = hs1[:19]
    return str(int(hs1[:20]) + int(hs2[:20]))

def add_tail(ts1, ts2):
    s = str(int(ts1[-9:]) + int(ts2[-9:]))
    return s[-9:]

def conv_int(s):
    if len(s) >= 9:
        return int(s[len(s)-9:])
    return int(s)

def is_pandigit(s):
    if len(s) != 9:
        return False
    l = list(s)
    l.sort()
    return ''.join(l) == '123456789'

def test():
    assert is_pandigit("789123456")
    assert is_pandigit("143726895")
    assert not is_pandigit("7891234")
    assert not is_pandigit("2")
    assert not is_pandigit("789123446")
    assert conv_int('123') == 123
    assert conv_int('111123456789') == 123456789

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
