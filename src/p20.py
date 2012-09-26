def fac(n):
    mul = 1
    for i in range(2,n+1):
        mul = mul * i
    return mul

def test():
    assert fac(1) == 1
    assert fac(2) == 2
    assert fac(3) == 6

def solve():
    n = fac(100)
    l = [int(c) for c in str(n)]
    return sum(l)

if __name__ == "__main__":
    test()
    print solve()
