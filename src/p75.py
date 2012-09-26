import math, time, mtools, sys

def solve():
    return one_angle_triangle(2000000)

def mark_similar(l, t, plist, lim):
    if not l[t]:
        #already more than 1 solution found
        #no need to search foundational solution
        for p in plist:
            n = p*t
            if n > lim:
                break
            l[n] = False
    elif l[t] != (0, 0):
        (a, b) = l[t]
        for p in plist:
            n = p*t
            if n > lim:
                break
            if not l[n]:
                continue
            na = p*a
            nb = p*b
            if l[n] != (0, 0):
                if l[n] != (na, nb):
                    l[n] = False
            else:
                l[n] = (na, nb)        

def one_angle_triangle(lim):
    rlim = lim / 2
    l = init_list(rlim+1)
    plist = mtools.sieve_primes(rlim/6+1)
    #print rlim, plist
    for t in range(6,rlim+1):
        if not l[t]:
            mark_similar(l, t, plist, rlim)
            continue
        up = int(math.sqrt(t))
        if up*up != t:
            up = up + 1
        down = int(math.sqrt(t/2)) + 1
        #print up, down
        for m in range(down, up):
            if t % m == 0:
                #print t, m
                n = t/m - m
                a = m*m - n*n
                b = 2*m*n
                if a > b:
                    tmp = a
                    a = b
                    b = tmp
                if l[t] != (0, 0):
                    if l[t] != (a, b):
                        #more than 1 solution
                        l[t] = False
                        break
                else:
                    #found a foundational solution
                    l[t] = (a, b)
        mark_similar(l, t, plist, rlim)
    l2 = [i for i in range(len(l)) if l[i] and l[i] != (0, 0)]
#    print l2, l
    return len(l2)

def test():
    assert 6 == one_angle_triangle(50)
    assert 8 == one_angle_triangle(70)
    one_angle_triangle(100)
    one_angle_triangle(120)

def init_list(size):
    return [(0,0) for x in range(size)]

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
