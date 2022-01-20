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


    for i in range (0, V):
        print(adj_matrix[i])

    return adj_matrix

graph = graph_input()