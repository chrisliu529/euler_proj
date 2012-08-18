def change(l):
    l.append(4)

def sum_hs(n):
    s = 0
    for i in range(1, n+1):
        s += 1.0/i
    return s

print sum_hs(10**7)
