#1 for christofides calculate mst
#2 get odd degree vertexes from mst, this must be even
#3 find the minimum weight maximal matching
#4 do union of the graph from 2 and 3
#5 do eulerian path of the graph from 4

from .Prim import LazyPrimMST
from .Graph import Graph, TSPGraph
from .MinHeapPQ import PQ, PQItem
from .DFS import DFS
from matplotlib import pyplot as plt

class Christofides:

    def __init__(self, G):
        self.G = G
        self.__perform()

    def __perform(self):
        # generate mst graph
        mst = LazyPrimMST(self.G)
        mstGraph = Graph(self.G.V)

        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        
        for edge in mst.mst.queue:
            mstGraph.addEdge(edge)

            stationFrom = self.G.getStation(edge.v)
            stationTo = self.G.getStation(edge.w)
            x = [stationFrom.lat, stationTo.lat]
            y = [stationFrom.lng, stationTo.lng]
            ax.plot(x, y, 'bo-', color='blue')
        

        # get all the odd stations
        oddVerticesStation = []
        x = []
        y = []
        for v in range(self.G.V):
            if len(mstGraph.adjacencies(v)) % 2 != 0:
                oddVerticesStation.append(v)
                x.append(self.G.getStation(v).lat)
                y.append(self.G.getStation(v).lng)

        ax.plot(x,y, 'o', color='black')

        
        minWeightMaximalEdges = self.__getMinWeightMatching(self.G, oddVerticesStation)
        
        minx = []
        miny = []
        for edge in minWeightMaximalEdges:
            print(edge)
            print(self.G)
            minx.append(self.G.getStation(edge.v).lat)
            miny.append(self.G.getStation(edge.v).lng) 
            minx.append(self.G.getStation(edge.w).lat)
            miny.append(self.G.getStation(edge.w).lng)
            ax.plot(minx, miny, ':', color='red')
            minx = []
            miny =[]
        plt.show()

        for edge in minWeightMaximalEdges:
            mstGraph.addEdge(edge)
        
        self.unionGraph = mstGraph

    
    def getPath(self):
        result = DFS(self.unionGraph, 0, self.G.getStations())
        return result.path, result.x, result.y

    def __getMinWeightMatching(self, G, oddVertices):
        # marked = [False for _ in range(G.V)]
        marked = {}
        for v in oddVertices:
            marked[v] = False

        amount = len(oddVertices) // 2

        minMaximalEdges = []

        gotten = 0

        print(G.minEdges.size())

        while gotten < amount:
            nextEdge = G.minEdges.delMin()
            print(nextEdge)
            print(gotten)
            if marked.get(nextEdge.v) == False and marked.get(nextEdge.w) == False:
                minMaximalEdges.append(nextEdge)
                marked[nextEdge.v] = True
                marked[nextEdge.w] = True
                gotten += 1
        return minMaximalEdges

        

        




