import time, os

def solve():
    f = open('sudoku.txt')
    s = f.read()
    f.close()
    lines = s.split('\n')
    grids = []
    for i in range(50):
        st = '\n'.join(lines[10*i+1:10*i+10])
        st = st.replace('0', '*')
        grids.append(st)

    sum = 0
    for grid in grids:
        print '---------\n', grid
        write_file(grid, 'grid')
        os.system('sudoku_solver grid > res')
        f = open('res')
        s = f.read()
        print '---------\n', s
        f.close()
        lines = s.split('\n')
        valid_line = lines[2]
        i = int(valid_line[0:3])
        print '---------\n', valid_line, i
        sum = sum + i
    return sum

def write_file(str, name):
    f = open(name, 'w')
    f.write(str)
    f.close()

def test():
    pass

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)

