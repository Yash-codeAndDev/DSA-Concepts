"""
Spanning Tree -> Tree/Graph having N nodes and N-1 edges and all nodes are rechable 
from each other

A minimum spanning tree (MST) is defined as a spanning tree that has the minimum 
weight among all the possible spanning trees
"""
import heapq

class PrimsAlgo:

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

    def getMST(self):
        
        vis = [False] * self.nodes
        mst = []
        pq = []
        # pq contains (weight, node, parent) since we have to push initial node 
        # in priority queue it should have weight = 0, node , and parent  = -1
        sum = 0
        heapq.heappush(pq , (0,0,-1))
        while pq:
            element = heapq.heappop(pq)
            # print("Popped Element : ",element)
            wt , node , parent = element
            
            if vis[node] == True:
                continue

            vis[node] = True
            sum += wt
            if parent != -1:
                mst.append((parent,node))

            for x in self.adjList[node]:
                adjNode = x[0]
                adjWeight = x[1]
                if vis[adjNode] == False:
                    heapq.heappush(pq, (adjWeight, adjNode, node))
                    
        print(mst)
        print("Total Weight : ",sum)

if __name__ == '__main__':
    obj = PrimsAlgo()
    obj.getMST()