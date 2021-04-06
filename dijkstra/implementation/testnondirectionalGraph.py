from Edge import Edge 
from Graph import Graph
from Dijkstra import DijkstraSP




# A = 0, B = 1, C = 2, D = 3 , E = 4

testGraph = Graph(5)

testGraph.addEdge(Edge(0, 1, 3)) #
testGraph.addEdge(Edge(0, 2, 1)) #

testGraph.addEdge(Edge(1, 2, 7)) #
testGraph.addEdge(Edge(1, 3, 5))
testGraph.addEdge(Edge(1, 4, 1))

testGraph.addEdge(Edge(2, 3, 2))

testGraph.addEdge(Edge(3, 4, 7))



def test_question():
    # print(testGraph.adjacencies(0))

    assert testGraph.adjacencies(0)[0].same(Edge(0, 1, 3)) == True
    assert testGraph.adjacencies(1)[0].same(Edge(0,1,3)) == True

    assert testGraph.adjacencies(0)[1].same(Edge(0, 2, 1)) == True
    assert testGraph.adjacencies(2)[0].same(Edge(0, 2, 1)) == True

    assert testGraph.adjacencies(1)[1].same(Edge(1, 2, 7)) == True
    assert testGraph.adjacencies(2)[1].same(Edge(1, 2, 7)) == True
    assert testGraph.adjacencies(1)[2].same(Edge(1, 3, 5)) == True
    assert testGraph.adjacencies(3)[0].same(Edge(1, 3, 5)) == True

    assert testGraph.adjacencies(1)[3].same(Edge(1, 4, 1)) == True
    assert testGraph.adjacencies(4)[0].same(Edge(1, 4, 1)) == True


    assert testGraph.adjacencies(2)[2].same(Edge(2, 3, 2)) == True
    assert testGraph.adjacencies(3)[1].same(Edge(2, 3, 2)) == True

    assert testGraph.adjacencies(3)[2].same(Edge(3, 4, 7)) == True
    assert testGraph.adjacencies(4)[1].same(Edge(3, 4, 7)) == True

# Testing dijstra result
def test_result():

    result = DijkstraSP(testGraph, 0)
    assert result.pathTo(1) == [1, 0] # [B, A]

    assert result.pathTo(2) == [2, 0] # [C, A]

    assert result.pathTo(3) == [3, 2, 0] # [D, C, A]

    assert result.pathTo(4) == [4, 1, 0] # [E, B, A]



    # assert testGraph.adjacencies(1)[0].same(Edge(1, 2, 7)) == True
    # assert testGraph.adjacencies(2)[0].same(Edge(1, 2, 7)) == True

    # print(testGraph.adjacencies(0)[0].same(Edge(0, 1, 3)))
    # print(testGraph.adjacencies(0)[0])