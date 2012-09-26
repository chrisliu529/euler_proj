import mtools, time, math

def solve():
    f = open('base_exp.txt')
    s = f.read()
    f.close()
    l = [process_line(line) for line in s.split('\n')]
    lb = list(l)
    l.sort(cmp=lambda x, y: cmp_exp(x, y), reverse=True)
    return lb.index(l[0])+1

def process_line(line):
    l = line.split(',')
    return (int(l[0]), int(l[1]))

def cmp_exp((b1, e1), (b2, e2)):
    return cmp(e1*math.log(b1), e2*math.log(b2))

def test():
    assert cmp_exp((632382,518061),(519432,525806)) > 0

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
