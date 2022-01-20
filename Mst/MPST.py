# midanim log(a1+a2+...)=log(a1)*log(a2)*...
# pas az khavase logarithm estefade mikonim ta sum ra be
# product tabdil konim. bejaye vazn har yal meghdare log(weight) ra
# gharar midahim. sepas yek algorithm mst ra ejra mikonim ta minimum total sum
# ra bedast avarad. chon sum ha dar inja log hastan pas be zarb tabdil mishavand
# ke haman minimum product ra bema barmigardanad.

import sys
import math

class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices                        
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]       

    def getMinimumKey(self, weight, visited):
        min = 9999
        for i in range(self.vertices):
            if weight[i] < min and visited[i] == False:
                min = weight[i]
                minIndex = i
        return minIndex

    def primsAlgo(self):
        weight = [9999] * self.vertices     
        MST = [None] * self.vertices        
        weight[0] = 0                       
        visited = [False] * self.vertices
        MST[0] = -1                         

        for _ in range(self.vertices):
            minIndex = self.getMinimumKey(weight, visited)
            visited[minIndex] = True

            for vertex in range(self.vertices):
                if self.graph[minIndex][vertex] > 0 and visited[vertex] == False and \
                weight[vertex] > self.graph[minIndex][vertex]:
                    weight[vertex] = self.graph[minIndex][vertex]
                    MST[vertex] = minIndex

        self.printMST(MST)

    def printMST(self, MST):
        s=1
        for i in range(1, self.vertices):
            s*=self.graph[i][MST[i]]
        print(s)
        

    def Logarithm(self,data):
        #jaygozari Log(weight) bejaye weight
        for i in range(len(data)):
            if(data[i]>=1):
                log_data.append(math.log(data[i]))
                
            else:
                log_data.append(0) 


if __name__ == '__main__':
    n=int(input())
    log_data=[]
    g  = Graph(n)

    for k in range(n):
        data=input()
        data=list(map(int, data.split()))
        g.Logarithm(data)
        g.graph[k]=data
    
    g.primsAlgo()