import sys
class Edge :
	def __init__(self, src, dst, weight) :
		 self.src = src 
		 self.dst = dst 
		 self.weight = weight

class Graph :
	def __init__(self, edge_list, node_cnt) :
		 self.edge_list = edge_list
		 self.node_cnt  = node_cnt

	def BellmanFord (self, src) :
		distance = [sys.maxsize] * self.node_cnt
		distance[src] = 0 

		for node in range(self.node_cnt) :
			for edge in self.edge_list :

				if (distance[edge.dst] > distance[edge.src] + edge.weight) :
					distance[edge.dst] = distance[edge.src] + edge.weight

		for edge in self.edge_list :

			if (distance[edge.dst] > distance[edge.src] + edge.weight) :
				print("MIA GETS RICH")
				quit()

		for node in range(self.node_cnt) : 
			if(distance[dest]==sys.maxsize):
				print("NO WAY")
				quit()
				
			if(node==dest):
				print(distance[node]-distance[source_node])
			


if __name__ == "__main__":
	data=list(map(int, input().split()))
	V,E=data[0],data[1]
	edge_list=[]
	
	for i in range(E):
		s = input()
		u,v,w = s.split()
		u,v,w = int(u)-1,int(v)-1,int(w)
		e=Edge(u,v,w)
		edge_list.append(e)


	sd = input().split()
	source=int(sd[0])-1
	dest=int(sd[1])-1


	
	source_node = source
	
	g = Graph(edge_list, V)
	g.BellmanFord(source_node)

