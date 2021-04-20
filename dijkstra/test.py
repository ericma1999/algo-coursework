from implementation.Graph import Graph, TSPGraph
from implementation.Edge import Edge
from implementation.MinHeapPQ import PQ


# testGraph = Graph(3)

# testGraph.addEdge(Edge(1,0,1))
# testGraph.addEdge(Edge(1,2,1))

# for v in range(testGraph.V):
#     if len(testGraph.adjacencies(v)) % 2 != 0:
#         print(v)


G = Graph(4)
G.addEdge(Edge(0,1,8))
G.addEdge(Edge(0,2,3))
G.addEdge(Edge(0,3, 4))

G.addEdge(Edge(1 ,2, 1))
G.addEdge(Edge(1,3, 4))

G.addEdge(Edge(2,3, 2))



marked = [False for _ in range(G.V)]
amount = G.V // 2
pq = PQ()

for vertex in range(G.V):
    for edge in G.adjacencies(vertex):
        pq.insert(edge)

gotten = 0 
maximalEdges = []
while gotten < amount:
    nextEdge = pq.delMin()

    if not (marked[nextEdge.endPoint()] or marked[nextEdge.otherEndPoint(nextEdge.endPoint())]):
        marked[nextEdge.endPoint()] = True 
        marked[nextEdge.otherEndPoint(nextEdge.endPoint())] = True
        gotten += 1
        maximalEdges.append(nextEdge)


for edge in maximalEdges:
    print(edge)