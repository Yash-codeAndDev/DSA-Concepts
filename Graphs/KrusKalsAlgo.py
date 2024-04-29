from DisjointSet import DisjointSet
class KruskalsAlgo:
    def __init__(self,n) -> None:
        self.queue = []
        self.N = n
    
    def addEdges(self):
        u = int(input("Enter u : "))
        v = int(input("Enter v : "))
        wt = int(input("Enter wt : "))
        self.queue.append((wt,u,v))


    def kruskalAlgo(self):

        # print(self.queue)
        sorted_queue = sorted(self.queue, key=lambda x: x[0])
        
        # print(sorted_queue)
        ds = DisjointSet(self.N)
        
        mst_weight = 0
        for x in sorted_queue:

            wt = x[0]
            u = x[1]
            v = x[2]

            if ds.findParent(u) != ds.findParent(v):
                mst_weight += wt
                ds.unionBySize(u,v)
            
        
        print(mst_weight)


if __name__ == "__main__":
    n = int(input("Enter the number of nodes: "))
    obj = KruskalsAlgo(n)
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        obj.addEdges()
    obj.kruskalAlgo()