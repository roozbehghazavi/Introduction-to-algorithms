# Python3 program to get maximum number of
# edges which can be removed such that each
# connected component of this tree will
# have an even number of vertices
from typing import List

# Utility method to do DFS of the graph
# and count edge deletion for even forest
def dfs(u: int, visit: List[bool]) -> int:
	
	global res, g

	visit[u] = True
	currComponentNode = 0

	# Iterate over all neighbor of node u
	for i in range(len(g[u])):
		v = g[u][i]
		
		if (not visit[v]):

			# Count the number of nodes in a subtree
			subtreeNodeCount = dfs(v, visit)

			# If returned node count is even, disconnect
			# the subtree and increase result by one.
			if (subtreeNodeCount % 2 == 0):
				res += 1

			# Else add subtree nodes in
			# current component
			else:
				currComponentNode += subtreeNodeCount

	# Number of nodes in current component
	# and one for current node
	return (currComponentNode + 1)

# Method returns max edge that we can remove,
# after which each connected component will
# have even number of vertices
def maxEdgeRemovalToMakeForestEven(N: int) -> int:
	
	# Create a visited array for DFS and make
	# all nodes unvisited in starting
	visit = [False for _ in range(N + 1)]

	# Calling the dfs from node-0
	dfs(0, visit)

	return res
	
# Utility function to add an undirected edge (u,v)
def addEdge(u: int, v: int) -> None:
	
	global g

	g[u].append(v)
	g[v].append(u)

# Driver code
if __name__ == "__main__":

	res = 0
	edges=[]
	ln=int(input())
	
	for k in range(ln-1):
		data=input()
		data=list(map(int, data.split()))
		edges.append(data)

	if(ln%2!=0):
		print(-1)
		quit()


	N = ln
	g = [[] for _ in range(N + 1)]
	
	for i in range(N-1):
		addEdge(edges[i][0], edges[i][1])

	print(maxEdgeRemovalToMakeForestEven(N))

# This code is contributed by sanjeev2552
