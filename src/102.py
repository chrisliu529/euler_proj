import time

def solve():
    f = open('triangles.txt')
    sl = f.read().split('\n')
    sl.remove('')
    f.close()
    pl = [conv_points(str) for str in sl]
    sum = 0
    for points in pl:
        if contain_origin(points[0], points[1], points[2]):
            sum = sum + 1
    return sum

def conv_points(str):
    li = [int(x) for x in str.split(',')]
    assert len(li) == 6
    l = []
    for i in range(0, 6, 2):
        l.append((li[i], li[i+1]))
    return l

def contain_origin(p1, p2, p3):
    p0 = (0, 0)
    s1 = abs(ts(p0, p1, p2))
    if s1 == 0:
        return False
    s2 = abs(ts(p0, p1, p3))
    if s2 == 0:
        return False
    s3 = abs(ts(p0, p2, p3))
    if s3 == 0:
        return False
    if abs(ts(p1, p2, p3)) == s1+s2+s3:
        return True
    return False

def ts((x1, y1), (x2, y2), (x3, y3)):
    return (x1-x3)*(y2-y3) - (y1-y3)*(x2-x3)

def test():
    assert [(1, 2), (3,4), (-5, 6)] == conv_points('1,2,3,4,-5,6')
    A = (-340,495)
    B = (-153,-910)
    C = (835,-947)
    assert contain_origin(A, B, C)
    X = (-175,41)
    Y = (-421,-714)
    Z = (574,-645)
    assert not contain_origin(X, Y, Z)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
