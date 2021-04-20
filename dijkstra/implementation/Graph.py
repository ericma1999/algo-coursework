from .Edge import Edge
from .Euclidean import euclidean_distance
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
        # print(self.adj)

    def adjacencies(self, v):
        return self.adj[v]


class TSPGraph(Graph):

    def __init__(self, V, stations):
        super().__init__(V)
        self.stations = []
        self.__createCompleteGraph(stations)

    def getStationName(self, index):
        return self.stations[index].getName()
    
    def getStations(self):
        return self.stations.copy()

    def getStation(self, index):
        return self.stations[index]

    def __createCompleteGraph(self, inputStations):
        for index, currentStation in enumerate(inputStations):
            for createdStationIndex, createdStation in enumerate(self.stations):
                distance = euclidean_distance(self.stations[createdStationIndex].lat, self.stations[createdStationIndex].lng, currentStation.lat, currentStation.lng)
                self.addEdge(Edge(index, createdStationIndex, distance))
            self.stations.append(currentStation)
