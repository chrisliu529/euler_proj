import time, math

def solve():
    return count_right_triangle(50)

def test():
#    assert form_B(2) == 2
#    assert form_B(5) == 8
    assert count_right_triangle(2) == 14

def count_right_triangle(n):
    cnt = n*n
    for x1 in range(n+1):
        for y1 in range(n+1):
            for x2 in range(n+1):
                for y2 in range(n+1):
                    if is_right(x1,x2,y1,y2):
                        cnt = cnt + 1
    print 'count_right_triangle(%d)=%d' % (n , cnt)
    return cnt
#    return form_A(n) + form_B(n)

def is_right(x1, x2, y1, y2):
    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0) or (x1 == x2 and y1 == y2):
        return False
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    return x1*x1+y1*y1+dx*dx+dy*dy == x2*x2+y2*y2

'''
def form_A(n):
    return 3*n*n

def form_B(n):
    for i in range(1, n):
        for x in range( ):
'''

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
