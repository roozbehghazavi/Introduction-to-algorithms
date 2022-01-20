#mst
import sys
import math

class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices                        
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]       

    def getMinimumKey(self, weight, visited):
        min = 100000000
        for i in range(self.vertices):
            if weight[i] < min and visited[i] == False:
                min = weight[i]
                minIndex = i
        return minIndex

    def primsAlgo(self):
        weight = [100000000] * self.vertices     
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
        s=0
        for i in range(1, self.vertices):
            s+=self.graph[i][MST[i]]
        print(s)

    def Distance(self,k,j):
        return abs(pts[k][1]-pts[j][1])+abs(pts[k][0]-pts[j][0])
        

if __name__ == '__main__':
    #sakhtane matrix mojaverat
    #hal in soal manande soal ghabl be komake
    #mst ast

    n=int(input())
    g = Graph(n)
    pts=[]
    datas=[]
    

    for i in range(n):
        data=input()
        data=list(map(int, data.split()))
        pts.append(data)
    
    for j in range(n):
        pt=pts[j]
        adj=[]
        for k in range(n):
            if(j==k):
                adj.append(0)
            else:
                adj.append(g.Distance(k,j))

        datas.append(adj)

    g.graph=datas
    g.primsAlgo()