# Multisource Shortest Path
# detect negative cycles


class FloydWarshal:

    def __init__(self) -> None:
        self.nodes = 0
        self.edges = 0
        self.adjMat = None

        self.createAdjList()
    
    def createAdjList(self):
        self.nodes = int(input("Enter Number of Nodes : "))
        self.edges = int(input("Enter Number of Edges : "))        
        
        self.adjMat = [ [0 if i==j else float('inf') for j in range(self.nodes)] for i in range(self.nodes)]


        for i in range(self.edges):
            u = int(input("From : "))
            v = int(input("To : "))
            wt = int(input("Weight : "))
            
            self.adjMat[u][v] = wt

    def printAdjMat(self):
        for i in range(self.nodes):
            print(self.adjMat[i])        

    def FloydWarshal(self):

        print("Initial Matrix")
        for x in self.adjMat:
            print(x)


        temp = self.adjMat

        for via in range(self.nodes):
            for i in range(self.nodes):
                for j in range(self.nodes):
                  
                    temp[i][j] = min(temp[i][j], 
                                    temp[i][via] + temp[via][j])
            

        # Checking -ve cycle
        for i in range(self.nodes):
            if temp[i][i] < 0:
                print("-ve Cycle Detected")
                break   
            
        print("Shortest Path Matrix")
        for x in temp:
            print(x)

if __name__ == '__main__':
    obj = FloydWarshal()
    # obj.printAdjMat()
    obj.FloydWarshal()