import math, time, mtools, sys

def count_list(l):
    d = {}
    for x in l:
        if d.has_key(x):
            n = d[x]
            d[x] = n + 1
        else:
            d[x] = 1
    r = []
    for x in d.iteritems():
        r.append(x)
    r.sort(cmp = lambda x,y: cmp(x[1], y[1]), reverse=True)
    return r

def solve():
    f = open('cipher1.txt')
    s = f.read()
    f.close()
    l = [int(w) for w in s.split(',')]
    max_str = '   ' #guessed
    cypher = ''
    for i in range(3):
        lp = [l[x] for x in range(i, len(l), 3)]
        cl = count_list(lp)
        print cl
        cy = chr(cl[0][0] ^ ord(max_str[i]))
        if cy.islower():
            cypher = cypher + cy
        else:
            print "guess cypher #%d wrong" % i
            sys.exit(2)
    dec = decode(l, cypher)
    des = ''.join([chr(x) for x in dec])
    print des
    return sum(dec)

def decode(l, c):
    code = [ord(x) for x in c]
    i = 0
    dec = []
    for x in l:
        dec.append(x^code[i])
        i = i + 1
        if (i % 3) == 0:
            i = 0
    return dec

def test():
    test_count_list()

def test_count_list():
    assert count_list([1,1]) == [(1,2)]

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

