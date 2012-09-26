import mtools, time, math

'''
 x2 - 2 y2 - x - 2 y = 0

by Dario Alejandro Alpern

X0 = 0
Y0 = -1

and also:
X0 = 1
Y0 = -1

Xn+1 = P Xn + Q Yn + K
Yn+1 = R Xn + S Yn + L

P = 3
Q = 4
K = 1
R = 2
S = 3
L = 0
'''
def solve():
    x0 = 0
    y0 = -1
    k = 0
    while True:
        x1 = 3*x0 + 4*y0 + 1
        y1 = 2*x0 + 3*y0
        xa = abs(x1)+1
        ya = abs(y1)-1
        if xa*(xa-1) == 2*ya*(ya+1):
            if xa >= 10**12:
                print xa, ya
                return ya+1
        x0 = x1
        y0 = y1
        k = k + 1
'''
def solve():
    t = 10**12
    while True:
        r = perfect_square(2*t*(t-1)+1)
        if r > 0 and r % 2 == 1:
            return (r+1)/2
        t = t+1
        if t % 1000000 == 0:
            print t
'''

def test():
    pass

def perfect_square(n):
    r = int(math.sqrt(n))
    if r*r == n:
        return r
    return 0

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
