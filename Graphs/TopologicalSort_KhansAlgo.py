class TopoSortKhansAlgo:

    def __init__(self) -> None:
        self.nodes = 0
        self.edges = 0
        self.adjList = None

        self.indegree = None
        self.createAdjList()
    
    def createAdjList(self):
        self.nodes = int(input("Enter Number of Nodes : "))
        self.edges = int(input("Enter Number of Edges : "))        
        self.adjList = [ [] for _ in range( self.nodes ) ]

        self.indegree = [0] * self.nodes

        print("Enter Edges : ")
        for i in range(self.edges):
            u = int(input("From : "))
            v = int(input("To : "))
            self.adjList[u].append(v)
            self.indegree[v] += 1 



    def printAdjList(self):
        for i in range(self.edges):
            print(" {} -> {} ".format(i, self.adjList[i]))            



    def printToposort(self):
        queue = []
        for i in range(self.nodes):
            if self.indegree[i] == 0:
                queue.append(i)

        while queue:
            
            n = queue.pop(0)
            print(n,end=" ")
            for x in self.adjList[n]:
                self.indegree[x] -= 1
                if self.indegree[x] == 0:
                    queue.append(x)
        

if __name__ == '__main__':
    obj = TopoSortKhansAlgo()

    # obj.printAdjList()
    obj.printToposort()
