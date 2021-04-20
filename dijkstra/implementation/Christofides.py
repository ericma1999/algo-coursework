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
                oddVerticesStation.append(self.G.getStation(v))
                x.append(self.G.getStation(v).lat)
                y.append(self.G.getStation(v).lng)

        ax.plot(x,y, 'o', color='black')
        
        # create graph of odd vertices
        oddDegreeVertexGraph = TSPGraph(len(oddVerticesStation), oddVerticesStation)

        


        minWeightMaximalEdges = self.__getMinWeightMatching(oddDegreeVertexGraph)
        
        minx = []
        miny = []
        for edge in minWeightMaximalEdges:
           minx.append(oddVerticesStation[edge.v].lat)
           miny.append(oddVerticesStation[edge.v].lng) 
           minx.append(oddVerticesStation[edge.w].lat)
           miny.append(oddVerticesStation[edge.w].lng)
           ax.plot(minx, miny, ':', color='red')
           minx = []
           miny =[]
        plt.show()

        for edge in minWeightMaximalEdges:

            oddVertexStationFrom = oddVerticesStation[edge.endPoint()].getName()
            oddVertexStationTo = oddVerticesStation[edge.otherEndPoint(edge.endPoint())].getName()
            edge.v = self.G.getStationIndexWithName(oddVertexStationFrom)
            edge.w = self.G.getStationIndexWithName(oddVertexStationTo)
            mstGraph.addEdge(edge)
        
        self.unionGraph = mstGraph

    
    def getPath(self):
        result = DFS(self.unionGraph, 0, self.G.getStations())
        return result.path, result.x, result.y



    def __getMinWeightMatching(self, G):
        marked = [False for _ in range(G.V)]
        amount = G.V // 2
        pq = PQ()

        for vertex in range(G.V):
            for edge in G.adjacencies(vertex):
                pq.insert(edge)
        
        gotten = 0 
        minMaximalEdges = []
        while gotten < amount:
            nextEdge = pq.delMin()
            print(nextEdge)
            if not marked[nextEdge.endPoint()] and not marked[nextEdge.otherEndPoint(nextEdge.endPoint())]:
               marked[nextEdge.endPoint()] = True 
               marked[nextEdge.otherEndPoint(nextEdge.endPoint())] = True
               gotten += 1
               minMaximalEdges.append(nextEdge)
        return minMaximalEdges

        

        




