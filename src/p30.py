import time

tab = [i**5 for i in range(0,10)]

def digits_sum(i1,i2,i3,i4,i5,i6):
    return tab[i1] + tab[i2] + tab[i3] + tab[i4] + tab[i5] + tab[i6]

def make_digits(i1,i2,i3,i4,i5,i6):
    return i1 + i2*10 + i3*100 + i4*1000 + i5*10000 + i6*100000

def solve():
    s = 0
    for i1 in range(0,10):
        for i2 in range(0,10):
            for i3 in range(0,10):
                for i4 in range(0,10):
                    for i5 in range(0,10):
                        for i6 in range(0,10):
                            d = make_digits(i1,i2,i3,i4,i5,i6)
                            if digits_sum(i1,i2,i3,i4,i5,i6) == d:
                                s = s + d
    # 1**5 is only one digit, not a sum
    return s-1

if __name__ == "__main__":
    t = time.time()
    print solve()
    print "(%s)" % (time.time() - t)
