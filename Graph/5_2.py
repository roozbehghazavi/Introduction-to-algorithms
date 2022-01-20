def find_edges(count):
    root = max(count)

    count_even = 0

    for cnt in count:
        if cnt % 2 == 0:
            count_even += 1

    if root % 2 == 0:
        count_even -= 1

    return count_even

def count_nodes(edge_list, n, m):
    count = [1 for i in range(0, n)]

    for i in range(m-1,-1,-1):
        count[edge_list[i][1]-1] += count[edge_list[i][0]-1]

    return find_edges(count)


ln=int(input())
edges=[]
for k in range(ln-1):
	data=input()
	data=list(map(int, data.split()))
	edges.append(data)

if(ln%2!=0):
	print(-1)
	quit()

print(count_nodes(edges,ln,ln))