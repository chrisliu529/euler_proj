import time

def get_pythagorean(limit):
    L = range(1,limit)
    for a in L:
        for b in L:
            for c in L:
                if (a + b > c) and (a*a+b*b==c*c) and (1000%(a+b+c)==0):
                    return (a,b,c)
    return (0,0,0)

def get_pythagorean2(limit):
    for m in range(1,limit):
        for n in range(m+1,limit):
            a = n*n-m*m
            b = 2*m*n
            c = m*m + n*n
            if (1000%(a+b+c)==0):
                return (a,b,c)
    return (0,0,0)

t = time.time()
(a,b,c) = get_pythagorean2(100)
k = 1000/(a+b+c)
print a*b*c*k*k*k
print time.time()-t
