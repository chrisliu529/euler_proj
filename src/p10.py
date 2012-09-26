import time,math

def is_prime2(m,l):
    lim = math.sqrt(m)
    for i in l:
        if i > lim:
            return True
        if m % i == 0:
            return False
    return True

def sum_prime(n):
    m = 3
    l = []
    l.append(2)
    l.append(3)
    while m < n:
        m = m+2
        if is_prime2(m,l):
            l.append(m)
    return sum(l)

def sum_prime2(n):
    l = range(0,n)
    lim = int(math.sqrt(n))+1
    i = 2
    while l[i] < lim:
        if l[i] > 0:
            for j in range(i+i,len(l),i):
                l[j] = 0
        i = i + 1
    return sum(l[2:])

def sum_prime3(n):
    l = [True for x in range(0,n)]
    lim = int(math.sqrt(n))+1
    for i in range(2,lim):
        if l[i]:
            for j in range(i+i,len(l),i):
                l[j] = False
    l2 = [x for x in range(2,n) if l[x]]
    return sum(l2)

assert sum_prime2(10) == 17
n = 2000000
t = time.time()
print sum_prime2(n)
print "(" + str((time.time()-t)) + ")"
