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
				if self.graph[minIndex][vertex] != 0 and visited[vertex] == False and \
				weight[vertex] > self.graph[minIndex][vertex]:
					weight[vertex] = self.graph[minIndex][vertex]
					MST[vertex] = minIndex

		self.printMST(MST)

	def printMST(self, MST):
		s=0
		for i in range(1, self.vertices):
			if(self.graph[i][MST[i]]!=-1):
				s+=self.graph[i][MST[i]]
		print(s)

	def Distance(self,k,j):
		return abs(pts[k][1]-pts[j][1])+abs(pts[k][0]-pts[j][0])
		
def graph_input():
	data=list(map(int, input().split()))
	V=data[0]
	E=data[1]
	cons_road=data[2]
	adj_matrix = []

	for i in range(0, V):
		temp = []
		for j in range(0, V):
			temp.append(0)
		adj_matrix.append(temp)
	
	for i in range(0, E):
		s = input()
		u, v, w = s.split()
		u = int(u)-1
		v = int(v)-1
		w = int(w)
		adj_matrix[v][u] = adj_matrix[u][v] = w
	
	for l in range(cons_road):
		inp=list(map(int, input().split()))
		a=inp[0]-1
		b=inp[1]-1
		adj_matrix[a][b] = adj_matrix[b][a] = -1


	# for i in range (0, V):
	# 	print(adj_matrix[i])

	return adj_matrix


if __name__ == '__main__':  
	city1 = graph_input()
	# print(city1)

	g=Graph(len(city1))
	g.graph=city1
	
	try:
		g.primsAlgo()
	except:
		print(-1)
	

	




