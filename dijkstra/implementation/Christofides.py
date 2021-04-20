#1 for christofides calculate mst
#2 get odd degree vertexes from mst, this must be even
#3 find the minimum weight maximal matching
#4 do union of the graph from 2 and 3
#5 do eulerian path of the graph from 4

from .Prim import LazyPrimMST
from .Graph import Graph, TSPGraph
from .MinHeapPQ import PQ, PQItem
from .DFS import DFS

class Christofides:

    def __init__(self, G):
        self.G = G
        self.__perform()

    def __perform(self):
        # generate mst graph
        mst = LazyPrimMST(self.G)
        mstGraph = Graph(self.G.V)
        for edge in mst.mst.queue:
            mstGraph.addEdge(edge)
        

        # get all the odd stations
        oddVerticesStation = []
        for v in range(self.G.V):
            if len(mstGraph.adjacencies(v)) % 2 != 0:
                oddVerticesStation.append(self.G.getStation(v))
        
        # create graph of odd vertices
        oddDegreeVertexGraph = TSPGraph(len(oddVerticesStation), oddVerticesStation)
        minWeightMaximalEdges = self.__getMinWeightMatching(oddDegreeVertexGraph)

        for edge in minWeightMaximalEdges:

            oddVertexStationFrom = oddVerticesStation[edge.endPoint()].getName()
            oddVertexStationTo = oddVerticesStation[edge.otherEndPoint(edge.endPoint())].getName()
            edge.v = self.G.getStationIndexWithName(oddVertexStationFrom)
            edge.w = self.G.getStationIndexWithName(oddVertexStationTo)
            mstGraph.addEdge(edge)
        
        self.unionGraph = mstGraph

    
    def getPath(self):
        result = DFS(self.unionGraph,  0, self.G.getStations())
        return result.path



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

            if not (marked[nextEdge.endPoint()] or marked[nextEdge.otherEndPoint(nextEdge.endPoint())]):
               marked[nextEdge.endPoint()] = True 
               marked[nextEdge.otherEndPoint(nextEdge.endPoint())] = True
               gotten += 1
               minMaximalEdges.append(nextEdge)
        return minMaximalEdges

        

        




