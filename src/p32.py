import time

def solve():
    l = []
    l2 = []
    # 2*3
    for i in range(11, 99):
        for j in range(123, 988):
            s = i*j
            if s >= 10000:
                continue
            if unique_number([i, j, s]):
                l.append(s)
                l2.append((i,j,s))
    # 1*4
    for i in range(2, 10):
        for j in range(1234, 4988):
            s = i*j
            if s >= 10000:
                continue
            if unique_number([i, j, s]):
                l.append(s)
                l2.append((i,j,s))
    print l2
    return sum(set(l))

def unique_number(l):
    s = [str(x) for x in l]
    s = ''.join(s)
    if s.find('0') >= 0:
        return False
    s = [ord(x) for x in s]
    return unique(s)

def unique(s):
    s.sort()
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

def test():
    assert not unique([1,1])
    assert unique([1,2])
    assert not unique([1,2,1])

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
