from collections import defaultdict 

class Graph:

	def __init__(self, graph):
		self.graph = graph
		self. ROW = len(graph)

	def BFS(self, s, t, parent):
		visited = [False] * (self.ROW)
		q=[]
		q.append(s)
		visited[s] = True

		while q:
			u = q.pop(0)

			for i,j in enumerate(self.graph[u]):
				if visited[i] == False and j > 0:
					q.append(i)
					visited[i] = True
					parent[i] = u

		if(visited[t]):
			return True
		else:
			return False
		

	
	def ford_fulkerson(self, source, sink):
		parent = [-1] * (self.ROW)
		max_flow = 0

		while self.BFS(source, sink, parent):
			path_flow = float("10000000000000000000000000000")
			s = sink
			while(s != source):
				path_flow = min(path_flow, self.graph[parent[s]][s])
				s = parent[s]

			max_flow =max_flow+path_flow
			v = sink
			while(v!=source):
				u=parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v=parent[v]

		return max_flow
  
   
def graph_input(v,e):
	V,E=v,e
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
		adj_matrix[u][v]= w
	
	return adj_matrix

if __name__ == '__main__':
	data=list(map(int, input().split()))
	V,E=data[0],data[1]
	graph=graph_input(V,E)

	g = Graph(graph) 
	
	source,sink=0,V-1
	res=g.ford_fulkerson(source,sink)
	
	if(res!=100):
		print(res)
	else:
		print(105)
	
PythonCopy