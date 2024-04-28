import heapq

class Dijkstra:

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
            w = int(input("Weight : "))
            self.adjList[u].append((v,w))
            self.adjList[v].append((u,w))
            


    def printAdjList(self):
        for i in range(self.nodes):
            print(" {} -> {} ".format(i, self.adjList[i]))            



    def shortestPath_Dijskstra(self):

        src = int(input("Enter Source : "))
        
        pq = []

        # make pq priority queue -> (dist, source)
        heapq.heappush(pq , (0,src))

        dist = [ float('inf')] * self.nodes
        dist[src] = 0

        while pq:

            dis, u = heapq.heappop(pq)

            for v, weight in self.adjList[u]:
                
                if dis + weight < dist[v]:
                    dist[v] = dis + weight
                    heapq.heappush(pq, (dist[v] , v))
        
        for i in range(self.nodes):
            print('{} -> {}'.format(i, dist[i]))

if __name__ == '__main__':
   obj = Dijkstra()
   obj.shortestPath_Dijskstra()