import math, time, mtools, sys

test_mat = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331] 
    ]

INFINITY = 1000000

def test():
    assert 2297 == minimal_sum_path(test_mat)

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
    dist = init_dist(m)
    sz = len(m)
    visited = [[False for i in range(sz)] for j in range(sz)]
    visited[0][0] = True

    for i in range(sz*sz - 1):
        min = INFINITY
        for r in range(sz):
            for c in range(sz):
                if not visited[r][c] and dist[r][c] < min:
                    min = dist[r][c]
                    vr = r
                    vc = c
        visited[vr][vc] = True
        d = dist[vr][vc]
        #check 4-ways
        #up
        if (vr > 0) and (not visited[vr-1][vc]) and (m[vr-1][vc] + d < dist[vr-1][vc]):
            dist[vr-1][vc] = m[vr-1][vc] + d
        #left
        if (vc > 0) and (not visited[vr][vc-1]) and (m[vr][vc-1] + d < dist[vr][vc-1]):
            dist[vr][vc-1] = m[vr][vc-1] + d
        #down
        if (vr < sz-1) and (not visited[vr+1][vc]) and (m[vr+1][vc] + d < dist[vr+1][vc]):
            dist[vr+1][vc] = m[vr+1][vc] + d
        #right
        if (vc < sz-1) and (not visited[vr][vc+1]) and (m[vr][vc+1] + d < dist[vr][vc+1]):
            dist[vr][vc+1] =  m[vr][vc+1] + d

    #format_print(dist)
    return dist[sz-1][sz-1]

def init_dist(m):
    sz = len(m)
    dist = [[0 for i in range(sz)] for j in range(sz)]
    dist[0][0] = m[0][0]
    for i in range(1, sz):
        dist[i][0] = dist[i-1][0] + m[i][0]
    for i in range(sz):
        for j in range(1, sz):
            dist[i][j] = dist[i][j-1] + m[i][j]
    #format_print(dist)
    return dist

def format_print(l):
    print '---------------------------------------------'
    for sl in l:
        print sl
    print '---------------------------------------------'

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
