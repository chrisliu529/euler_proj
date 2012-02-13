import math, time, mtools, sys

def solve():
    l = construct([6], [9,8,7,10], [5,4,3,2,1], 14, 15)
    print l
    assert len(l) == 15
    assert verify(l)
    s = [str(x) for x in l]
    return ''.join(s)

def test():
    r = construct([4], [6,5], [3,2,1], 9, 9)
    assert [4,3,2, 6,2,1, 5,1,3] == r

def construct(gon_ring, extern_ring, intern_ring, total, total_size):
    #print 'construct(%s, %s, %s, %s)' % (gon_ring, extern_ring, intern_ring, total)
    sz = len(gon_ring)
    if sz == total_size:
        return gon_ring
    if sz % 3 == 0:
        #select an element in external ring
        for i in range(len(extern_ring)):
            e = extern_ring[i]
            gon_ring.append(e)
            extern_ring.remove(e)
            r = construct(gon_ring, extern_ring, intern_ring, total, total_size)
            if r:
                return r
            extern_ring.insert(i, e)
            gon_ring.pop()
    elif sz % 3 == 1:
        if sz < 2:
            #select an element in internal ring
            for i in range(len(intern_ring)):
                e = intern_ring[i]
                gon_ring.append(e)
                intern_ring.remove(e)
                r = construct(gon_ring, extern_ring, intern_ring, total, total_size)
                if r:
                    return r
                intern_ring.insert(i, e)
                gon_ring.pop()
        else:
            #copy internal element has been set
            gon_ring.append(gon_ring[sz-2])
            r = construct(gon_ring, extern_ring, intern_ring, total, total_size)
            if r:
                return r
            gon_ring.pop()
    elif sz % 3 == 2:
        #calc the last element in the line
        e = total - gon_ring[sz-1] - gon_ring[sz-2]
        removed = False
        if intern_ring != []:
            if e not in intern_ring:
                return None
            idx = intern_ring.index(e)
            intern_ring.remove(e)
            removed = True
        elif e != gon_ring[1]:
            return None
        gon_ring.append(e)
        r = construct(gon_ring, extern_ring, intern_ring, total, total_size)
        if r:
            return r
        gon_ring.pop()
        if removed:
            intern_ring.insert(idx, e)

def verify(l):
    sl = [[l[i],l[i+1],l[i+2]] for i in range(0,15,3)]
    suml = [sum(x) for x in sl]
    return len(set(suml)) == 1

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

