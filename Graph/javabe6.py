from copy import deepcopy


def BFSCheck(visited, currentRow, column, matrixRow, matrixColumn):
    
    if (currentRow < 0 or column < 0 or currentRow >= matrixRow or column >= matrixColumn) : return False

    if (visited[currentRow][column]) : return False
 
    return True
 

def BFS(matrix, visited, row, column):
    matrixRow = len(matrix)
    matrixColumn = len(matrix[0])
    numOfLake = 0
    Queue = []

    Queue.append([row, column])
    visited[row][column] = True
    

    while (len(Queue) > 0):
        cellTmp = Queue[0]
        Queue.pop(0)
        currentX = cellTmp[0]
        currentY = cellTmp[1]
        numOfLake += 1


        # left neighbor
        tempX = currentX - 1 
        tempY = currentY
        if (BFSCheck(visited, tempX, tempY, matrixRow, matrixColumn)):
            if matrix[tempX][tempY] != '*':
                Queue.append([tempX, tempY])
                visited[tempX][tempY] = True

        # up neighbor
        tempX = currentX 
        tempY = currentY + 1
        if (BFSCheck(visited, tempX, tempY, matrixRow, matrixColumn)):
            if matrix[tempX][tempY] != '*':
                Queue.append([tempX, tempY])
                visited[tempX][tempY] = True

        # right neighbor
        tempX = currentX + 1
        tempY = currentY 
        if (BFSCheck(visited, tempX, tempY, matrixRow, matrixColumn)):
            if matrix[tempX][tempY] != '*':
                Queue.append([tempX, tempY])
                visited[tempX][tempY] = True

        # down neighbor
        tempX = currentX
        tempY = currentY -1
        if (BFSCheck(visited, tempX, tempY, matrixRow, matrixColumn)):
            if matrix[tempX][tempY] != '*':
                Queue.append([tempX, tempY])
                visited[tempX][tempY] = True                                    


    return numOfLake % 10               

def split(word):
    return [char for char in word]



inp = list(map(int, input().split()))
row, column = inp[0], inp[1]

matrix = []
for i in range(row):
    matrix.append(split(input()))

copyMatrix = deepcopy(matrix)        

visited = [[ False for i in range(column)] for i in range(row)]
for i in range(row):
    for j in range(column):
        visited = [[ False for i in range(column)] for i in range(row)]
        if matrix[i][j] == '*':
            tmp = BFS(matrix, visited, i, j) 
            copyMatrix[i][j] =  tmp


for i in range(row):
    for j in range(column):
        print(copyMatrix[i][j], end='')
    print()