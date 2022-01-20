import sys



INF = sys.maxsize


def floydWarshall(graph,V):


	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))


	for k in range(V):


		for i in range(V):


			for j in range(V):

				dist[i][j] = min(dist[i][j],
								dist[i][k] + dist[k][j]
								)
	printSolution(dist)



def printSolution(dist):
	print("Following matrix shows the shortest distances\
between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print("%7s" % ("INF"))
			else:
				print("%7d\t" % (dist[i][j]))
			if j == V-1:
				print("")


if __name__ == '__main__':
	graph =[]
	data=list(map(int, input().split()))
	V,E=data[0],data[1]
	for i in range(0, E):
		s = input()
		u,v,w = s.split()
		u,v,w = int(u)-1,int(v)-1,int(w)
		graph.append([u,v,w])

	sd = input().split()

	source=int(sd[0])-1
	dest=int(sd[1])-1
	
	
floydWarshall(graph,V)

