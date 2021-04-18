# from Graph import Graph
# from Edge import Edge
from .MinHeapPQ import PQ, PQItem
from .UnionFind import UnionFind


class NearestNeighbor:
    def __init__(self, G):
        self.bestScore = -1
        self.bestPaths = []
        self.marked = [False for _ in range(G.V)]
        for starting in range(G.V):
            self.uf = UnionFind(G.V)
            self.__nearestNeighbor(starting, G)
            print("\n\n")

    def __nearestNeighbor(self, v, G):
        vertexAmount = 0
        path = [G.getStationName(v)]
        score = 0

        currentVertex = v
        nextEdge = None
        while vertexAmount < G.V - 1:
            pq = PQ()
            for edge in G.adjacencies(currentVertex):
                pq.insert(edge)
            while not pq.isEmpty() and vertexAmount < G.V:
                nextEdge = pq.delMin()
                if self.uf.find(currentVertex, nextEdge.otherEndPoint(nextEdge.endPoint())):
                    continue
                else:
                    break
            print(nextEdge)
            print(G.getStationName(nextEdge.otherEndPoint(nextEdge.endPoint())))
            print(nextEdge.otherEndPoint(nextEdge.endPoint()))
            path.append(G.getStationName(nextEdge.otherEndPoint(nextEdge.endPoint())))

            self.uf.union(currentVertex, nextEdge.otherEndPoint(nextEdge.endPoint()))
            currentVertex = nextEdge.otherEndPoint(nextEdge.endPoint())
            
            vertexAmount += 1
            score += nextEdge.weight
            print(path)
            print(vertexAmount)
            print(score)

        if self.bestScore == -1:
            self.bestScore = score
            self.bestPaths = path
    
        if score < self.bestScore:
            self.bestScore = score
            self.bestPaths = path

    def getPaths(self):
        return self.bestPaths
    
    def getScore(self):
        return self.bestScore


# testGraph = Graph(4)
# testGraph.addEdge(Edge(0, 1, 9))
# testGraph.addEdge(Edge(0, 2, 18))
# testGraph.addEdge(Edge(0, 3, 5))

# testGraph.addEdge(Edge(1, 2, 1))
# testGraph.addEdge(Edge(1, 3, 7))

# testGraph.addEdge(Edge(2, 3, 3))

# test = NearestNeighbor(testGraph)
# print(test.getScore())
# print(test.getPaths())