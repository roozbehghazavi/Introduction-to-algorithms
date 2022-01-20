# Calculate the size of the largest `+` formed by 1's
def calculateSize(grid):
 
    # `left[j][j]` stores the maximum number of consecutive 1's
    # present at the left of `grid[i][j]` (including `grid[i][j]`)
    left = [[0 for x in range(N)] for y in range(N)]
 
    # `right[j][j]` stores the maximum number of consecutive 1's
    # present at the right of `grid[i][j]` (including `grid[i][j]`)
    right = [[0 for x in range(N)] for y in range(N)]
 
    # `top[j][j]` stores the maximum number of consecutive 1's
    # present at the top of `grid[i][j]` (including `grid[i][j]`)
    top = [[0 for x in range(N)] for y in range(N)]
 
    # `bottom[j][j]` stores the maximum number of consecutive 1's
    # present at the bottom of `grid[i][j]` (including `grid[i][j]`)
    bottom = [[0 for x in range(N)] for y in range(N)]
 
    # initialize the above matrices
    for i in range(N):
        # initialize the first row of the top matrix
        top[0][i] = grid[0][i]
 
        # initialize the last row of the bottom matrix
        bottom[N - 1][i] = grid[N - 1][i]
 
        # initialize the first column of the left matrix
        left[i][0] = grid[i][0]
 
        # initialize the last column of the right matrix
        right[i][N - 1] = grid[i][N - 1]
 
    # fill all cells of the above matrices
    for i in range(N):
        for j in range(1, N):
            # fill the left matrix
            if grid[i][j] == 1:
                left[i][j] = left[i][j - 1] + 1
 
            # fill the top matrix
            if grid[j][i] == 1:
                top[j][i] = top[j - 1][i] + 1
 
            # fill the bottom matrix
            if grid[N - 1 - j][i] == 1:
                bottom[N - 1 - j][i] = bottom[N - j][i] + 1
 
            # fill the right matrix
            if grid[i][N - 1 - j] == 1:
                right[i][N - 1 - j] = right[i][N - j] + 1
 
    # `bar` stores the length of the longest `+` found so far
    bar = 0
 
    # compute the longest plus
    for i in range(N):
        for j in range(N):
            # find minimum of left(i, j), right(i, j), top(i, j), bottom(i, j)
            len = min(top[i][j], bottom[i][j], left[i][j], right[i][j])
 
            # largest `+` would be formed by a cell that has a maximum value
            if len - 1 > bar:
                bar = len - 1
 
    return bar
 
 
if __name__ == '__main__':
 
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]
 
    N = 10
    bar = calculateSize(grid)
 
    # 4 directions of length `4×bar+1` for a middle cell
    if bar:
        print("The largest plus of 1's has a size of", (4 * bar + 1))