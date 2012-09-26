'''
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
'''

import time

def count_angle(p):
    t = p/2
    cnt = 0
    for a in range(1, t/2+1):
        for b in range(t-a, t):
            if is_right_angle(a, b, p-a-b):
                cnt = cnt + 1
    return cnt

def solve():
    max = 0
    max_p = 0
    for p in range(12, 1000, 2):
        t = count_angle(p)
        if t > max:
            max = t
            max_p = p
    return max_p

def is_right_angle(a, b, c):
    return a*a + b*b == c*c

def test():
    assert is_right_angle(3, 4, 5)
    assert 3 == count_angle(120)

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
