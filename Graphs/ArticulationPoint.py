"""
Articulation Point :

Node on whoes removal graph breaks down in multiple component
"""
class ArticulationPoint:
    def __init__(self) -> None:
        self.nodes = 0
        self.adjList = None
        self.time = 0
        self.articPoint = {}    
        self.createAdjList()
    
    def createAdjList(self):
        self.nodes = int(input("Enter Number of Nodes : "))
        self.edges = int(input("Enter Number of Edges : "))        
        self.adjList = [ [] for _ in range( self.nodes ) ]

        self.addEdge(0,1)
        self.addEdge(1,2)
        self.addEdge(2,3)
        self.addEdge(3,0)

        self.addEdge(3,4)
        self.addEdge(4,5)

        self.addEdge(5,6)
        self.addEdge(5,7)
        self.addEdge(6,8)
        self.addEdge(7,8)

        self.addEdge(8,9)
        self.addEdge(9,10)
        self.addEdge(10,11)
        self.addEdge(9,11)
            
        
       
    def addEdge(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

   
    def dfs(self,u,parent,vis,disc,low,mark):
        disc[u] = self.time
        low[u] = self.time
        vis[u] = True

        self.time += 1
        child = 0
        for x in self.adjList[u]:
            if parent == u:
                continue
            
            if vis[x] == False:
                self.dfs(x,u,vis,disc,low,mark)
                low[u] = min(low[u], low[x])
                if low[x] >= disc[u] and parent != -1:
                    mark[u] = True

                child += 1
            else:
                low[u] = min(low[u],disc[x])
            
            if child > 1 and  parent == -1:
                mark[u] = True
 
    def findArticulationPoint(self):
        vis = [False] * self.nodes

        discvory = [0] * self.nodes    
        low = [0] * self.nodes
        mark = [False] * self.nodes 
        for i in range(self.nodes):
            if vis[i] == False:
                self.dfs(i,-1,vis,discvory,low,mark)

        for i in range(self.nodes):
            if mark[i] == True:
                print(i, end=" ")

if __name__ == '__main__':
    obj = ArticulationPoint()
    obj.findArticulationPoint()