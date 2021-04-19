class BruteForce:
    def __init__(self, G):

        self.totalVertex = G.V
        self.G = G
        self.best_score = -1
        self.best_path = []

        # loop through all possible staring points
        for v in range(G.V):
            vertexCount = 1
            visited = [False for _ in range(G.V)]
            visited[v] = True
            path = [v]
            score = 0

            self.__possibleEdges(G.adjacencies(v), visited, path, score, vertexCount)                
    
    def __possibleEdges(self, edges, visited, currentPath, currentScore, vertexCount):
        for edge in edges:
                self.__travelEachEdge(edge, visited.copy(), currentPath.copy(), currentScore, vertexCount)


    def __travelEachEdge(self, edge, visited, path, score, vertexCount):
        if vertexCount == self.totalVertex:
            if score < self.best_score or self.best_score == -1:
                self.best_score = score
                self.best_path = path
            return

        toVisit = edge.otherEndPoint(edge.endPoint())
        if not visited[toVisit]:
            vertexCount += 1
            score += edge.weight
            path.append(toVisit)
            visited[toVisit] = True
            self.__possibleEdges(self.G.adjacencies(toVisit), visited, path, score, vertexCount)