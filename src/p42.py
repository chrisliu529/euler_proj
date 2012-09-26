import time

def solve():
    f = open('words.txt')
    s = f.read()
    l = s.split(',')
    l = [w[1:len(w)-1] for w in l]
    length = [len(w) for w in l]
    length.sort()
    max = length[len(length)-1]

    triangle = generate(max*26)
    v = [value(w) for w in l]
    cnt = 0
    for x in v:
        if x in triangle:
            cnt = cnt + 1
    return cnt

def generate(lim):
    t = 0
    n = 1
    l = []
    while t < lim:
        t = n*(n+1)/2
        n = n + 1
        l.append(t)
    return l

def value(w):
    sum = 0
    for c in w:
        sum = sum + ord(c) - ord('A') + 1
    return sum

def test():
    assert value('SKY') == 55
    assert generate(60) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
