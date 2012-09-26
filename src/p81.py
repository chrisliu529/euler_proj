import math, time, mtools, sys

test_mat = [
	[131,673,234,103,18],
	[201,96,342,965,150],
	[630,803,746,422,111],
	[537,699,497,121,956],
	[805,732,524,37,331] 
]

def test():
    assert 2427 == minimal_sum_path(test_mat)

def solve():
    f = open('matrix.txt')
    s = f.read()
    f.close()
    mat = get_matrix(s)
    assert len(mat) == 80
    return minimal_sum_path(mat)

def get_matrix(s):
    l = s.split('\n')
    l.remove('')
    return [conv_int(x.split(',')) for x in l]

def conv_int(l):
    return [int(x) for x in l]

def minimal_sum_path(m):
    l = m[0]
    sz = len(l)
    for i in range(1, len(l)):
        l[i] = l[i] + l[i-1]
    for i in range(1, len(m)):
        m[i][0] = m[i][0] + m[i-1][0]
        l = m[i]
        for j in range(1, len(l)):
            c1 = l[j-1]
            c2 = m[i-1][j]
            if c1 < c2:
                l[j] = l[j] + c1
            else:
                l[j] = l[j] + c2
    return m[sz-1][sz-1]        

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
