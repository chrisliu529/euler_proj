T1 = [
[3],
[7, 5],
[2, 4, 6],
[8, 5, 9, 3]
]

T2 =[
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[04,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

def is_triangle(t):
    for i in range(0, len(t)):
        if len(t[i]) != i+1:
            return False
    return True

def max_triangle(t):
    assert is_triangle(t)
    v = [[t[0][0]]]
    for i in range(1,len(t)):
        tv = []
        lim = len(t[i])
        for j in range(0,lim):
            et = t[i][j]
            if (j == 0):
                elem = v[i-1][0] + et
            elif (j == lim-1):
                elem = v[i-1][lim-2] + et
            else:
                a = v[i-1][j]
                b = v[i-1][j-1]
                if a > b:
                    elem = a + et
                else:
                    elem = b + et
            tv.append(elem)
        v.append(tv)
    l = v[len(v)-1]
    l.sort(reverse=True)
    #print l
    return l[0]


def test():
    assert max_triangle(T1) == 23

if __name__ == "__main__":
    test()
    print max_triangle(T2)
