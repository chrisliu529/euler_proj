import time

def transform(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n + 1

def trans_times(n,tab):
    i = 1
    n = transform(n)
    while n != 1:
        if tab.has_key(n):
            return i+tab[n]
        n = transform(n)
        i = i + 1
    return i

def main():
    max = 0
    max_t = 0
    tab = {}
    for i in range(1,1000000):
        t = trans_times(i,tab)
        tab[i] = t
        if t > max_t:
            max_t = t
            max = i
    print max, max_t

if __name__ == "__main__":
    t = time.time()
    main()
    print "("+str(time.time()-t)+")"
