import heapq

class BellmanFord:

    def __init__(self) -> None:
        self.nodes = 0
        self.edges = 0
        self.adjList = None

        self.createAdjList()
    
    def createAdjList(self):
        self.nodes = int(input("Enter Number of Nodes : "))
        self.edges = int(input("Enter Number of Edges : "))        
        self.adjList = [] 

        print("Enter Edges : ")
        for i in range(self.edges):
            u = int(input("From : "))
            v = int(input("To : "))
            w = int(input("Weight : "))
            self.adjList.append((u,v,w))
          


    def printAdjList(self):
        for i in range(self.nodes):
            print(" {} -> {} ".format(i, self.adjList[i]))            


    def shortestPath(self):
        dist = [float('inf')] * self.nodes
  
        src = int(input("Enter Source : "))
        dist[src] = 0

        for i in range(self.nodes - 1):

            for itr in self.adjList:
                u , v , wt = itr[0],itr[1],itr[2]

                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt


        # Nth relaxation to check -ve cycles
        for itr in self.adjList:
            u , v , wt = itr[0],itr[1],itr[2]
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                print("-ve cycle detected")
                break

        print("Shortest distance from source: ")
        for i in range(self.nodes):
            print("{} -> {}".format(src,dist[i]))

if __name__ == '__main__':
   obj = BellmanFord()
   obj.shortestPath()