class BridgeInGraph:
    def __init__(self) -> None:
        self.nodes = 0
        self.adjList = None
        self.steps = 1    
        self.createAdjList()
    
    def createAdjList(self):
        self.nodes = int(input("Enter Number of Nodes : "))
        self.edges = int(input("Enter Number of Edges : "))        
        self.adjList = [ [] for _ in range( self.nodes ) ]


        
        # print("Enter Edges : ")
        # for i in range(self.edges):
        #     u = int(input("From : "))
        #     v = int(input("To : "))
        self.addEdge(0,1)
        self.addEdge(1,2)
        self.addEdge(2,3)
        self.addEdge(3,0)

        self.addEdge(3,4)
        self.addEdge(4,5)

        self.addEdge(5,6)
        self.addEdge(5,8)
        self.addEdge(6,7)
        self.addEdge(7,8)
        self.addEdge(7,9)

        self.addEdge(9,10)
        self.addEdge(10,11)
        self.addEdge(9,11)
            
    def addEdge(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def dfs(self, u , parent, vis, tim, low,bridges):
        
        vis[u] = True
        tim[u] = self.steps 
        low[u] = self.steps
        self.steps += 1

        for x in self.adjList[u]:
            if x == parent:
                continue
            if vis[x] == False:
                self.dfs(x,u,vis,tim,low,bridges)
                low[u] = min(low[u],low[x])
                if low[x] > tim[u]:
                    bridges.append((x,u))
            else:
                low[u] = min(low[u],low[x])




    def NumberOfBridges(self):

        vis = [False] * self.nodes

        timeOfInsertion = [0] * self.nodes
        lowestInsertionTime = [0] * self.nodes
        bridges = []

        self.dfs(0,-1,vis,timeOfInsertion,lowestInsertionTime,bridges)

        print(bridges)



if __name__ == '__main__':
    obj = BridgeInGraph()
    obj.NumberOfBridges()