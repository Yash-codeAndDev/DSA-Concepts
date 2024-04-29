class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n+1)
        self.parent = [i for i in range(n+1)]
        self.CompSize = [1 for i in range(n+1)]
    
    def findParent(self, u):
        if u == self.parent[u]:
            return u

        self.parent[u] = self.findParent( self.parent[u])
        return self.parent[u]
    
    def unionByRank(self, u , v):
        up_u = self.findParent(u)
        up_v = self.findParent(v)

        if up_u == up_v:
            return
        if self.rank[up_u] < self.rank[up_v]:
            self.parent[up_u] = up_v
        elif self.rank[up_u] > self.rank[up_v]:
            self.parent[up_v] = up_u
        else:
            self.parent[up_v] = up_u
            self.rank[up_u] +=1
        
         
    def unionBySize(self, u , v):
        up_u = self.findParent(u)
        up_v = self.findParent(v)

        if up_u == up_v:
            return
        if self.CompSize[up_u] < self.CompSize[up_v]:
            self.parent[up_u] = up_v
            self.CompSize[up_v] += self.CompSize[up_u]
        else:
            self.parent[up_v] = up_u
            self.CompSize[up_u] += self.CompSize[up_v]

if __name__ == '__main__':
   
    obj = DisjointSet(7)
    """
    obj.unionByRank(1,2)
    obj.unionByRank(2,3)
    obj.unionByRank(4,5)
    obj.unionByRank(6,7)
    obj.unionByRank(5,6)
    
    if obj.findParent(3) == obj.findParent(7):
        print("Same Parent")
    else:
        print("Different Parent")
            
    obj.unionByRank(3,7)

    
    if obj.findParent(3) == obj.findParent(7):
        print("Same Parent")
    else:
        print("Different Parent")
         
    """
    
    obj.unionBySize(1,2)
    obj.unionBySize(2,3)
    obj.unionBySize(4,5)
    obj.unionBySize(6,7)
    obj.unionBySize(5,6)
    
    if obj.findParent(3) == obj.findParent(7):
        print("Same Parent")
    else:
        print("Different Parent")
            
    obj.unionBySize(3,7)

    
    if obj.findParent(3) == obj.findParent(7):
        print("Same Parent")
    else:
        print("Different Parent")
            