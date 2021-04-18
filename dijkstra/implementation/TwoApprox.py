from .Prim import LazyPrimMST
from .Graph import Graph
from .DFS import DFS

class TwoApprox:

    def __init__(self, G):
        print(G)
        mst = LazyPrimMST(G)
        dfsGraph = Graph(G.V)

        for edge in mst.mst.queue:
            print(edge)
            dfsGraph.addEdge(edge)

        result = DFS(dfsGraph, 0, G.getStations())
        self.path = result.path
    
    def getPath(self):
        return self.path