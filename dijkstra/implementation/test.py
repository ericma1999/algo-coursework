from Edge import Edge 
from Graph import Graph
from Dijkstra import DijkstraSP

testGraph = Graph(8)

testGraph.addEdge(Edge(0 , 1, 5))
testGraph.addEdge(Edge(0 , 7, 8))
testGraph.addEdge(Edge(0 , 4, 9))

testGraph.addEdge(Edge(1, 3, 15))
testGraph.addEdge(Edge(1, 2, 12))
testGraph.addEdge(Edge(1, 7, 4))

testGraph.addEdge(Edge(2, 3, 3))
testGraph.addEdge(Edge(2, 6, 11))


testGraph.addEdge(Edge(3, 6, 9))


testGraph.addEdge(Edge(4, 7, 5))
testGraph.addEdge(Edge(4, 5, 4))
testGraph.addEdge(Edge(4, 6, 20))

testGraph.addEdge(Edge(5, 2, 1))
testGraph.addEdge(Edge(5, 6, 13))

testGraph.addEdge(Edge(7, 2, 7))
testGraph.addEdge(Edge(7, 5, 6))

result = DijkstraSP(testGraph, 0)


def test_graph():
    # test base case
    assert result.pathTo(0) == [0]
    assert result.lengthTo(0) == 0

    assert result.pathTo(1) == [1, 0]
    assert result.lengthTo(1) == 5

    assert result.pathTo(7) == [7, 0]
    assert result.lengthTo(7) == 8

    assert result.pathTo(4) == [4, 0]
    assert result.lengthTo(4) == 9

    assert result.pathTo(5) == [5, 4, 0]
    assert result.lengthTo(5) == 13

    assert result.pathTo(2) == [2, 5, 4, 0]
    assert result.lengthTo(2) == 14

    assert result.pathTo(3) == [3, 2 , 5, 4, 0]
    assert result.lengthTo(3) == 17

    assert result.pathTo(6) == [6, 2, 5 ,4 , 0]
    assert result.lengthTo(6) == 25