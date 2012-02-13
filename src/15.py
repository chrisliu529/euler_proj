def fac(x):
    if x == 1:
        return 1
    else:
        return x*fac(x-1)

def test():
    l = [(1,1),(2,2),(3,6)]
    for (input,output) in l:
        assert output == fac(input)

if __name__ == "__main__":
    test()
    print fac(40)/(fac(20)*fac(20))
