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
        self.result = result
    
    def getPath(self):
        return self.result.path, self.result.x, self.result.y