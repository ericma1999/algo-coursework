class UnionFind:
    def __init__(self, size):
        #init
        self.id = []
        self.size =[]
        for i in range (10):
            self.id.append(i)
            self.size.append(1)

        #root
    def getRoot(self,i):
        root = i
        while root!=self.id[root]:
            root=self.id[root]
        # path compression
        # traverse and update when calling root when value is not same as root
        while i != root:
            next = self.id[i]
            self.id[i] = root
            i = next
        return root

    #find
    def find(self,u,v):
        return self.getRoot(u)==self.getRoot(v)


    #union
    def union(self,u,v):
        r_u=self.getRoot(u)
        r_v=self.getRoot(v)
        if r_u==r_v: return
        if self.size[r_u]<self.size[r_v]:
            self.id[r_u]=r_v
            self.size[r_v]+=self.size[r_u]
        else:
            self.id[r_v]=r_u
            self.size[r_u]+=self.size[r_v]
        