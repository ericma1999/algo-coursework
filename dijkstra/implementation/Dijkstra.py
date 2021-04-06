class QueueItem():
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight
    
    def __ge__(self, other):
        return self.weight >= other.weight

    def __gt__(self, other):
        return self.weight > other.weight
    
    def __le__(self, other):
        return self.weight <= other.weight
    
    def __lt__(self, other):
        return self.weight < other.weight
        
class MinPQ():
    def __init__(self):
        self.queue = []
    
    def insert(self, vertex, weight):
        self.queue.append(QueueItem(vertex, weight))
        self.queue.sort(reverse = True)
    
    def delMin(self):
        return self.queue.pop()
    
    def isEmpty(self):
        return self.queue == []

    def contains(self, vertex):
        for queueItem in self.queue:
            if queueItem.vertex == vertex:
                return True
        return False

    def decreaseKey(self, vertex, distanceTo):
        for queueItem in self.queue:
            if queueItem.vertex == vertex:
                queueItem.weight = distanceTo
                self.queue.sort(reverse = True)
class DijkstraSP:

    def __init__(self, G, s):
        self.edgeTo = [None for v in range (0, G.V)]
        # -1 for infinity since weight cannot be negative
        self.distTo = [-1 for v in range(0, G.V)]
        self.distTo[s] = 0


        self.pq = MinPQ()
        self.pq.insert(s, 0)
        self.starting = s

        while not self.pq.isEmpty():
            v = self.pq.delMin().vertex
            for e in G.adjacencies(v):
                self.__relax(e)

    def __relax(self, e):
        v = e.endPoint()
        w = e.otherEndPoint(v)

        if self.distTo[w] > self.distTo[v] + e.getWeight() or self.distTo[w] == -1:
            self.distTo[w] = self.distTo[v] + e.getWeight()
            self.edgeTo[w] = e

            if self.pq.contains(w):
                self.pq.decreaseKey(w, self.distTo[w])
            else:
                self.pq.insert(w, self.distTo[w])



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
















