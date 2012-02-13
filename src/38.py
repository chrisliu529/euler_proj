#encoding=utf-8

'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

import time

def sum_mul(n):
    l = []
    for i in range(1, 6):
        l.append(n*i)
    return pandigits(l)

def pandigits(l):
    s = ''
    i = 0
    for x in l:
        s = s + str(x)
        i = i + 1
        if len(s) == 9 and s.find('0') < 0 and pandigits2(l[:i]):
            return int(s)
        elif len(s) > 9:
            return 0
    return 0

def pandigits2(l):
    lb = []
    for x in l:
        lb = lb + separate_ones(x)
    if len(set(lb)) == 9:
        return True
    return False
 
def separate_ones(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n / 10
    return l

def solve():
    max = 0
    for i in range(2, 10000):
        t = sum_mul(i)
        if (t > max):
            max = t
    return max

def test():
    assert separate_ones(123) == [3, 2, 1]
    assert pandigits2([123,456,789])
    assert pandigits2([192,384,576])
    assert pandigits([123,456,789]) == 123456789
    assert pandigits([122,456,789]) == 0
    assert pandigits([1223,456,789]) == 0
    assert pandigits([12,456,789]) == 0
    assert sum_mul(192) == 192384576
    assert sum_mul(9) == 918273645

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
