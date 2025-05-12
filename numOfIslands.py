

grid = [
    ["1", "1", "1", "1"],
    ["1", "1", "0", "0"],
    ["0", "0", "0", "1"],
    ["0", "0", "1", "1"]
]






def enclaves(grid):
    enclave = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c]= "1"





'''

def numOfIslands(grid):
    islands = 0
    maxislandsize = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "1":
                islandsize = dfs(grid,r,c)
                islands += 1
                if islandsize > maxislandsize:
                    maxislandsize = islandsize
    return islands, maxislandsize


def dfs(grid,row,col) -> int:

    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == "0":
        return 0

    size = 1
    grid[row][col] = "0"
    size +=dfs(grid, row - 1, col)
    size +=dfs(grid,row+1, col)
    size +=dfs(grid,row,col+1)
    size +=dfs(grid,row,col-1)
    return size


print(numOfIslands(grid))



'''









































































def numOfIslands(grid):
    island = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "1":
                bfs(grid, r, c)
                island += 1
    return island


def dfs(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == "0":
        return
    grid[row][col] = "0"
    #transverse_stack = [(row-1, col),(row+1,col),(row,col+1),(row,col-1)] used recursive as oppose to iterative approach
    dfs(grid, row-1, col)
    dfs(grid, row, col-1)
    dfs(grid,row+1,col)
    dfs(grid,row, col+1)

'''
def bfs(grid, row,col):
    que = deque([(row, col)])
    while que:
        r,c = popleft()

        if row > 0 and col > 0 and row <= len(grid) and col <= len(grid[0]) and grid[row][col] == "0":
            continue

    grid[r][c] = "0"

    bfs.append((row, col + 1))
    bfs.append(grid, row, col - 1)
    bfs.append(grid, row + 1, col)
    bfs.append(grid, row - 1, col)



'''




#print(numOfIslands(grid))

'''