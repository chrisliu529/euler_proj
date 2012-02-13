import math, time, mtools, sys

test_mat = [
	[131,673,234,103,18],
	[201,96,342,965,150],
	[630,803,746,422,111],
	[537,699,497,121,956],
	[805,732,524,37,331] 
]

test_mat2 = [
	[1,5,7,1],
	[1,1,1,10],
	[3,5,1,1],
	[10,10,10,10]
]

def test():
    assert [[1,2],[1,2]] == trans([[1,1],[2,2]])
    assert 994 == minimal_sum_path2(test_mat)
    assert 5 == minimal_sum_path2(test_mat2)

def solve():
    f = open('matrix.txt')
    s = f.read()
    f.close()
    mat = get_matrix(s)
    assert len(mat) == 80
    return minimal_sum_path2(mat)

def get_matrix(s):
    l = s.split('\n')
    l.remove('')
    return [conv_int(x.split(',')) for x in l]

def conv_int(l):
    return [int(x) for x in l]

def minimal_sum_path2(mat):
    m = trans(mat)
    l = m[0]
    sz = len(m)
    for i in range(1, len(m)-1):
        pl = m[i-1]
        l = m[i]
        lb = list(l)
        for j in range(len(l)):
            l[j] = detect_min(pl, lb, j)
        #print l, lb, pl
    #print m
    pl = m[sz-2]
    l =  m[sz-1]
    l2 = [(pl[i]+l[i]) for i in range(len(l))]
    return min(l2)

def detect_min(pl, l, j):
    min = pl[j] + l[j]
    for i in range(j):
        v = pl[i] + sum(l[i:j+1])
        if v < min:
            min = v

    for i in range(j+1, len(l)):
        v = pl[i] + sum(l[j:i+1])
        if v < min:
            min = v

    return min

def trans(mat):
    w = len(mat[0])
    h = len(mat)
    l = []
    m = []
    for i in range(w):
        for j in range(h):
            l.append(mat[j][i])
        m.append(l)
        l = []
    return m

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

