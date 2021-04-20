class DFS:
    path = []
    x = []
    y = []
    def __init__(self, G, s, names):
        self.names = names
        self.starting = s
        self.marked = [False for v in range(0, G.V)]
        self.edgeTo = [-1 for v in range (0, G.V)]
        self.path.append(self.names[s].getName())
        self.x.append(self.names[s].lat)
        self.y.append(self.names[s].lng)
        self.__dfs(G,s)
    
    def __dfs(self, G, v):
        self.marked[v] = True
        for w in G.adjacencies(v):
            currentPoint = w.otherEndPoint(w.endPoint())
            if (not self.marked[currentPoint]):
                self.path.append(self.names[currentPoint].getName())
                self.x.append(self.names[currentPoint].lat)
                self.y.append(self.names[currentPoint].lng)
                self.__dfs(G,currentPoint)
                self.edgeTo[currentPoint] = v
    
    def hasPathTo(self, v):
        return self.marked[v]

    # build the path backwards 
    def pathTo(self, v):
        if (not self.hasPathTo(v)): return None
        path = []
        x = v
        while (x != self.starting):
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.starting)
        return path