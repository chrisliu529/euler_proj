import time, math, mtools

def solve():
    cnt = 0
    for i in range(1, 10000):
        c = is_lychrel(i)
        if c == 0:
            cnt = cnt + 1
            #print i, c
    return cnt

def is_lychrel(n):
    for i in range(1,40):
        n = reverse_add(n)
        if is_palindrome(n):
            return i
    return 0

def reverse_add(n):
    return n + reverse_int(n)

def reverse_int(n):
    s = str(n)
    return int(reverse_str(s))

def reverse_str(s):
    rs = ''
    l = list(s)
    l.reverse()
    for x in l:
        rs = rs + x
    return rs

def is_palindrome(n):
    return n == reverse_int(n)

def test():
    assert reverse_str('47') == '74'
    assert reverse_add(47) == 121
    assert is_palindrome(4994)
    assert not is_palindrome(4995)
    assert is_lychrel(349) != 0
    assert is_lychrel(196) == 0

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
