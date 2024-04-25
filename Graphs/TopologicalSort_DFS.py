class TopoSortDFS:

    def __init__(self) -> None:
        self.nodes = 0
        self.edges = 0
        self.adjList = None
        self.createAdjList()
    
    def createAdjList(self):
        self.nodes = int(input("Enter Number of Nodes : "))
        self.edges = int(input("Enter Number of Edges : "))        
        self.adjList = [ [] for _ in range( self.nodes ) ]

        print("Enter Edges : ")
        for i in range(self.edges):
            u = int(input("From : "))
            v = int(input("To : "))
            self.adjList[u].append(v)


    def printAdjList(self):
        for i in range(self.edges):
            print(" {} -> {} ".format(i, self.adjList[i]))            


    def dfs(self ,n , stack, vis):
        vis[n] = True

        for x in self.adjList[n]:
            if vis[x] == False:
                self.dfs(x,stack,vis)
        
        stack.append(n)

    def printToposort(self):

        stack = []
        vis = [False] * self.nodes

        for i in range(self.nodes):
            if vis[i] == False:
                self.dfs( i, stack, vis)


        print("Topological Order : ")
        print(stack[::-1])


if __name__ == '__main__':
    obj = TopoSortDFS()

    obj.printAdjList()
    obj.printToposort()