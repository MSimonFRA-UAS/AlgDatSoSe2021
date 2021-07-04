class Graph:

    def __init__(self, n_vertices):
        self.n = n_vertices
        self.adj = [[0 for column in range(n_vertices)] for row in range(n_vertices)]

    def is_allowed(self, v, col, c):
        for i in range(self.n):
            if self.adj[v][i] == 1 and col[i] == c:
                print('Node', v, 'Color tested: ', col[i])
                return False
        return True

    def color(self, k, col, v):
        if v == self.n:
            return True
        for c in range(1, k + 1):
            if self.is_allowed(v, col, c):
                col[v] = c
                print('Node', v, 'Color assigned: ', col[v])
                if self.color(k, col, v + 1):
                    return True
                col[v] = 0

    def graph_coloring(self, k):
        col = [0] * self.n
        if self.color(k, col, 0) is None:
            print('No', k, '-coloring exists.' )
            return False
        print(k, '-coloring found. Assigned colors:')
        for c in col:
            print(c)
        return True


if __name__ == '__main__':
    g = Graph(4)
    g.adj = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    k = 3
    g.graph_coloring(k)
