class Queue():
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)


class BFS:
    def __init__(self, G, s):
        self.starting = s
        self.distToSource = [-1 for v in range(0, G.V)]
        self.edgeTo = [-1 for v in range(0, G.V)]
        self.__bfs(G, s)

    def __bfs(self, G, s):
        q = Queue()
        q.enqueue(s)
        self.distToSource[s] = 0
        while(not q.isEmpty()):
            v = q.dequeue()

            for w in G.adjacencies(v):
                index = w.otherEndPoint(v)
                if (self.distToSource[index] == -1):
                    q.enqueue(index)
                    self.distToSource[index] = self.distToSource[v] + 1
                    self.edgeTo[index] = v
    
    def hasPathTo(self, v):
        return self.distToSource[v] != -1
    

    ## BFS calculates shortest path so this is the shortest path
    def pathTo(self, v):
        if (not self.hasPathTo(v)): return None

        path = []
        x = v
        while (x != self.starting):
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.starting)
        return path


    ## BFS calculates shortest path so this is the shortest length
    def lengthTo(self, v):
       if (not self.hasPathTo(v)): return None

       return self.distToSource[v] 
