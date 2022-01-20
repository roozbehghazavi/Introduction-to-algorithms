import sys
class Graph:
	def __init__(self, vertices):
		self.V = vertices 
		self.graph = []

	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])
		
	def printarray(self, res):
		print("Vertex Distance from Source") 
		for i in range(self.V): 
			print("{0}\t\t{1}".format(i, res[i])) 

		if(res[dest]-res[source]==sys.maxsize):
			print("NO WAY")

		else:
			print(res[dest]-res[source])

	
	def BellmanFord(self, src):
		res=[sys.maxsize for i in range(V+1)]
		res[src] = 0

		for i in range(self.V - 1):
			for u,v,w in self.graph:
				if((res[u]+w<res[v]) and (res[u] != sys.maxsize)):
					res[v]=res[u]+w

		#Negative Cycle Detector
		for u,v,w in self.graph:
			if((res[u] != sys.maxsize) and (res[u] + w < res[v])):
				print("MIA GETS RICH")
				quit()
						
		self.printarray(res)


if __name__ == '__main__':
	data=list(map(int, input().split()))
	V,E=data[0],data[1]

	g1=Graph(V)

	for i in range(0, E):
		s = input()
		u,v,w = s.split()
		u,v,w = int(u)-1,int(v)-1,int(w)
		g1.addEdge(u,v,w)

	sd = input().split()

	source=int(sd[0])-1
	dest=int(sd[1])-1
	print(g1.graph)
	g1.BellmanFord(0)


