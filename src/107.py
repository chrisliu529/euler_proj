import mtools

max_weight = 1000

def conv_elem(x):    
    if x == '-':
        return max_weight
    return int(x)

def conv_line(l):
    return [conv_elem(x) for x in l]
            
def read_matrix(fn):
    f = file(fn)
    return [conv_line(line.strip().split(',')) for line in f]

def edge(e):
    if e == max_weight:
        return 0
    return e

class Graph:
    def __init__(self, fn):
        self.matrix = read_matrix(fn)
        self.points = len(self.matrix)
    
    def edges_weight(self):
        w = 0
        for i in range(self.points):
            for j in range(i):
                w += edge(self.matrix[i][j])
        return w
    
    def prim_mst(self):
        p = self.points
        st = [-1 for x in range(p)]
        fr = range(p)
        wt = [max_weight for x in range(p+1)]
        st[0] = 0
        min = 0
        while (min != p):
            v = min
            st[min] = fr[min]
            w = 0
            min = p
            while (w < p):
                if st[w] == -1:
                    if self.matrix[v][w] < wt[w]:
                        wt[w] = self.matrix[v][w]
                        fr[w] = v
                    if wt[w] < wt[min]:
                        min = w
                w += 1
        self.mst = st
        self.mst_wt = wt

    def mst_weight(self):
        self.prim_mst()        
        return sum([edge(x) for x in self.mst_wt])
    
    def optimized_flow(self):
        ew = self.edges_weight()
        mw = self.mst_weight()
        print ew, mw
        return ew - mw        

def mst_prim(m):
    pass

def sum_edges(m):
    pass

def optimized_flow(fn):
    pass

class q107: 
    def test(self):
        g = Graph('107_test.txt')
        assert 10 == g.edges_weight()
        f = g.optimized_flow()
        assert 6 == f

    def solve(self):
        g = Graph('107_network.txt')
        return g.optimized_flow()

if __name__ == "__main__":
    mtools.run(q107())
