# from Graph import Graph
# from Edge import Edge
from .MinHeapPQ import PQ, PQItem


class NearestNeighbor:
    def __init__(self, G):
        self.bestScore = -1
        self.bestPaths = []

        for starting in range(G.V):
            self.marked = [False for _ in range(G.V)]
            self.marked[starting] = True
            self.__nearestNeighbor(starting, G, G.getStation(starting).lat, G.getStation(starting).lng)
            print("\n\n")

    def __nearestNeighbor(self, v, G, startLat, startLng):
        vertexAmount = 0
        path = [G.getStationName(v)]
        score = 0
        x = [startLat]
        y = [startLng]
        currentVertex = v
        nextEdge = None
        while vertexAmount < G.V - 1:
            pq = PQ()
            for edge in G.adjacencies(currentVertex):
                pq.insert(edge)
            while not pq.isEmpty() and vertexAmount < G.V:
                nextEdge = pq.delMin()

                if self.marked[nextEdge.otherEndPoint(nextEdge.endPoint())]:
                    continue
                else:
                    break
            
            x.append(G.getStation(nextEdge.otherEndPoint(nextEdge.endPoint())).lat)
            y.append(G.getStation(nextEdge.otherEndPoint(nextEdge.endPoint())).lng)

            path.append(G.getStationName(nextEdge.otherEndPoint(nextEdge.endPoint())))
            self.marked[nextEdge.otherEndPoint(nextEdge.endPoint())] = True

            currentVertex = nextEdge.otherEndPoint(nextEdge.endPoint())
            
            vertexAmount += 1
            score += nextEdge.weight

        if self.bestScore == -1 or score < self.bestScore:
            self.bestScore = score
            self.bestPaths = path
            self.x = x
            self.y = y

    def getPaths(self):
        return self.bestPaths
    
    def getScore(self):
        return self.bestScore