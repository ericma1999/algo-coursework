class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = []
        for _ in range (0, V):
            self.adj.append([])

    def addEdge(self, e):
        v = e.endPoint()
        w = e.otherEndPoint(v)
        self.adj[v].append(e)
        # self.adj[w].append(e)
        # we have to swap here because we have to relax its outgoing edges, if we don't swap the direction around it would relax the wrong end
        self.adj[w].append(e.swap())

    def adjacencies(self, v):
        return self.adj[v]