"""
Strongly Connected Component : Component of Directed Graph that has path 
from every vertex to every other vertex in that component

Kosaraju Algorithm : 
    1) Sort Edges on Basis of Finishing Time
    2) Reverse Graph
    3) Do DFS
"""

class KosarajuAlgo:
    def __init__(self) -> None:
        self.adjList = None
        self.nodes = 0
        self.createGraph()
    def createGraph(self):
        
        self.nodes = int(input("Enter number of Nodes : "))
        edges = int(input("Enter number of Edges : "))
        
        self.adjList = [ [] for i in range(self.nodes)]

        print("Enter edges : ")
        for i in range(edges):
            u = int(input("u : "))
            v = int(input("v : "))
            self.adjList[u].append(v)

    def dfs(self, n, vis, stack):
        vis[n] = True
        for x in self.adjList[n]:
            if vis[x] == False:
                self.dfs(x,vis,stack)

        stack.append(n)

    def dfs2(self, n, vis, adjLs):
        vis[n] = True
        for x in adjLs[n]:
            if vis[x] == False:
                self.dfs2(x,vis,adjLs)


    def KosarajuAlgo(self):

        scc = 0
        # Step 1
        vis = [False] * self.nodes
        stack = []
        for i in range(self.nodes):
            if vis[i] == False:
                self.dfs(i,vis,stack)
        
        # print("Sorted Nodes according to Finishing Time  : ")
        # print(stack)



        # Step 2
        # print("Adjacency List : ")
        # for i in range(self.nodes):
        #     print("{} , {}".format(i,self.adjList[i]))

        reverseAdjList = [ [] for i in range(self.nodes)]
        for i in range(self.nodes):
            for x in self.adjList[i]:
                reverseAdjList[x].append(i)

        # print("Reverse Adjacency List")
        # for i in range(self.nodes):
        #     print("{}-> {}".format(i,reverseAdjList[i]))
        # print()
        
       
       
        # Step 3
        vis = [False] * self.nodes
        while stack:
            element = stack.pop()
            if vis[element] == False:
                scc += 1
                self.dfs2(element,vis,reverseAdjList)
                # print("Visited Array : ")
                # print("{} , {}".format(element,vis))
                # print()
        print("Strongly Connected Component : ",scc)



if __name__ == '__main__':
    obj = KosarajuAlgo()
    obj.KosarajuAlgo()