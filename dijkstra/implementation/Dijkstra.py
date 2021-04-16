from .MinHeapPQ import PQ as MinPQ
from .MinHeapPQ import PQItem

class DijkstraSP:

    def __init__(self, G, s):
        self.edgeTo = [None for v in range (0, G.V)]
        # -1 for infinity since weight cannot be negative
        self.distTo = [-1 for v in range(0, G.V)]
        self.distTo[s] = 0


        self.pq = MinPQ()
        self.pq.insert(PQItem(s, 0))
        self.starting = s

        while not self.pq.isEmpty():
            v = self.pq.delMin().name
            for e in G.adjacencies(v):
                self.__relax(e)

    def __relax(self, e):
        v = e.endPoint()
        w = e.otherEndPoint(v)
        # print(w)
        if self.distTo[w] > self.distTo[v] + e.getWeight() or self.distTo[w] == -1:
            self.distTo[w] = self.distTo[v] + e.getWeight()
            self.edgeTo[w] = e

            if self.pq.contains(w):
                self.pq.decreaseKey(w, self.distTo[w])
                # print("will decrease key")
            else:
                self.pq.insert(PQItem(w, self.distTo[w]))



    # def hasPathTo(self, v):
    #     return self.distToSource[v] != -1
    

    def pathTo(self, v):
        path = []
        x = v
        while (x != self.starting):
            path.append(x)
            x = self.edgeTo[x].endPoint()
        path.append(self.starting)
        return path

    def lengthTo(self, v):
       return self.distTo[v] 