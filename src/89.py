import time

def solve():
    f = open('roman.txt')
    s = f.read()
    numbers = s.split('\n')
    sub_sum = 0
    for n in numbers:
        i = read_roman(n)
        #print i
        new_n = write_roman(i)
        sub = (len(n) - len(new_n))
        assert sub >= 0
        sub_sum = sub_sum + sub
    return sub_sum

def test():
    test_read_roman()
    test_write_roman()

def test_read_roman():
    assert 1 == read_roman('I')
    assert 4 == read_roman('IIII')

def test_write_roman():
    assert 'I' == write_roman(1)
    assert 'IV' == write_roman(4)

def read_roman(s):
    n = 0
    i = 0
    for i in range(len(s)-1):
        v = roman_value(s[i])
        if v >= roman_value(s[i+1]):
            n = n + v
        else:
            n = n - v
    n = n + roman_value(s[len(s)-1])
    return n

def write_roman(n):
    s = ''
    if n >= 1000:
        t = n / 1000
        n = n % 1000
        if t > 0:
            s = s + write_thousand(t)
    if n >= 100:
        t = n / 100
        n = n % 100
        if t > 0:
            s = s + write_hundred(t)
    if n >= 10:
        t = n / 10
        n = n % 10
        if t > 0:
            s = s + write_ten(t)
    if n > 0:
        s = s + write_last(n)
    return s

def write_thousand(t):
    return 'M'*t

def write_hundred(t):
    return write_digits(t, 'C', 'D', 'M')

def write_ten(t):
    return write_digits(t, 'X', 'L', 'C')

def write_last(t):
    return write_digits(t, 'I', 'V', 'X')

def write_digits(t, one, five, ten):
    #print t
    assert (t > 0 and t < 10)
    if t <= 3:
        return one*t
    if t == 4:
        return one + five
    if t == 5:
        return five
    if t <= 8:
        return five + one*(t-5)
    if t == 9:
        return one + ten

'''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
'''
def roman_value(c):
    if c == 'I':
        return 1
    if c == 'V':
        return 5
    if c == 'X':
        return 10
    if c == 'L':
        return 50
    if c == 'C':
        return 100
    if c == 'D':
        return 500
    if c == 'M':
        return 1000

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
