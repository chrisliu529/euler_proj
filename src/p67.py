import math, time, mtools, sys

def is_triangle(t):
    for i in range(0, len(t)):
        if len(t[i]) != i+1:
            return False
    return True

def max_triangle(t):
    assert is_triangle(t)
    v = [[t[0][0]]]
    for i in range(1,len(t)):
        tv = []
        lim = len(t[i])
        for j in range(0,lim):
            et = t[i][j]
            if (j == 0):
                elem = v[i-1][0] + et
            elif (j == lim-1):
                elem = v[i-1][lim-2] + et
            else:
                a = v[i-1][j]
                b = v[i-1][j-1]
                if a > b:
                    elem = a + et
                else:
                    elem = b + et
            tv.append(elem)
        v.append(tv)
    l = v[len(v)-1]
    l.sort(reverse=True)
    #print l
    return l[0]

def solve():
    f = open('triangle.txt')
    s = f.read()
    f.close()
    lines = s.split('\n')
    lines.pop()
    t = [convert(l.split()) for l in lines]
    return max_triangle(t)

def convert(l):
    return [int(x) for x in l]

def test():
    T1 = [
    [3],
    [7, 5],
    [2, 4, 6],
    [8, 5, 9, 3]
    ]
    assert max_triangle(T1) == 23

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
