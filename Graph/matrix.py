matrix=[]
dimensions=input()


row, column = int(dimensions[0]), int(dimensions[2])

for i in range(row):
    data=input()
    data=list(data)
    matrix.append(data)

print(matrix)
