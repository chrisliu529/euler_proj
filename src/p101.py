import mtools, time, math
from scipy import *

def solve():
    return sum_op(u, 13)

def sum_op(f, k):
    l = [f(n) for n in range(1, k)]
    #print l
    l2 = [op(l, i) for i in range(1, k-1)]
    li = map(make_int, l2[:len(l2)-1])
    #print li
    return sum(li)

def make_int(e):
    if e > 0:
        if abs(e - math.floor(e)) > 0.5:
            return int(math.ceil(e))
        return int(e)
    else:
        if abs(e - math.ceil(e)) > 0.5:
            return int(math.floor(e))
        return int(e)        

def u(n):
    s = 1
    for i in range(1, 11):
        s = s + ((-1)**i)*(n**i)
    return s

def op(l, n):
    f = gen_fun(l, n)
    l2 = [f(i) for i in range(1, n+2)]
    #print l2
    assert l[:n] == l2[:n]
    return l2[n]

def gen_fun(l, n):
    #print n
    if n == 1:
        return (lambda x: l[0])
    if n == 9:
        #scipy doesn't have enough presion
        #the values below are computed with Matlab
        coefficient = [1111, -28831, 352528, -2514688, 11126621, -30669221, 50572225, 
                       -44806465, 15966721]
        return make_f(n, coefficient)
    if n == 10:
       coefficient = [54, -1319, 18149, -157772, 902054, -3416929, 8409499, -12753575, 
                      10628639, -3628799] 
       return make_f(n, coefficient)
    m = square_matrix(n)
    src_matrix = mat(m)
    dm = [[l[i]] for i in range(n)]
    dst_matrix = mat(dm)
    res = linalg.solve(src_matrix, dst_matrix)
#    '''
    #print conv_str(m)
    #print conv_str(dm)
    #print res
#    '''
    coefficient = map(make_int,to_list(res))
    #print coefficient
    return make_f(n, coefficient)

def make_f(n, coefficient):
    def f(x):
        s = 0
        i = n - 1
        for c in coefficient:
            assert i >= 0
            s = s + c*(x**(i))
            i = i - 1
        return s
    return f

def conv_str(m):
    s = '[' + conv_row(m[0])
    for i in range(1, len(m)):
        s = s + ';' + conv_row(m[i])
    s = s + ']'
    return s

def conv_row(r):
    s = str(r[0])
    for i in range(1, len(r)):
        s = s + ',' + str(r[i])
    return s

def square_matrix(n):
    l = [[1 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            l[i][j] = (i+1)**j
        l[i].reverse()
    return l

def to_list(m):
    l = []
    for r in m:
        l.append(r[0])
    return l

def test():
    assert [[1, 1], [2, 1]] == square_matrix(2)
    assert [[1, 1, 1], [4, 2, 1], [9, 3, 1]] == square_matrix(3)
    assert [7, 6] == to_list([[7], [6]])
    assert 683 == make_int(683.00000000002183)
    assert -1984312 == make_int(-1984311.99999987)
    ret = sum_op(lambda x:x**3, 6)
    #print ret
    assert ret == 74

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
