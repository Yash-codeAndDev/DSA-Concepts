class TopoSortDFS:

    def __init__(self) -> None:
        self.nodes = 0
        self.edges = 0
        self.adjList = None

        self.stack = None
        self.createAdjList()
    
    def createAdjList(self):
        self.nodes = int(input("Enter Number of Nodes : "))
        self.edges = int(input("Enter Number of Edges : "))        
        self.adjList = [ [] for _ in range( self.nodes ) ]

        print("Enter Edges : ")
        for i in range(self.edges):
            u = int(input("From : "))
            v = int(input("To : "))
            w = int(input("Weight : "))
            self.adjList[u].append((v,w))


    def printAdjList(self):
        for i in range(self.nodes):
            print(" {} -> {} ".format(i, self.adjList[i]))            


    def dfs(self ,n , stack, vis):
        vis[n] = True

        for i in self.adjList[n]:
            x = i[0]
            if vis[x] == False:
                self.dfs(x,stack,vis)
        
        stack.append(n)

    def printToposort(self):

        self.stack = []
        vis = [False] * self.nodes

        for i in range(self.nodes):
            if vis[i] == False:
                self.dfs( i, self.stack, vis)

        self.stack.reverse()
        print(self.stack)


    def shortestPath(self):
        
        source = int(input("Enter Source Node : "))
        distArr = [ float('inf')] * self.nodes
        distArr[source] = 0

        while self.stack:

            ele = self.stack.pop(0)
            # print("Popped Element : ",ele)
            # print("-> Adjacent Nodes")
            for temp in self.adjList[ele]:
                print("\t ",temp)
                if distArr[ele] + temp[1] < distArr[temp[0]]:
                    distArr[temp[0]] = distArr[ele] + temp[1]
                # print("\t dist Array : ",distArr)

        print(distArr)


if __name__ == '__main__':
    obj = TopoSortDFS()

    obj.printAdjList()
    obj.printToposort()

    obj.shortestPath()