
grid = [
    ["1", "1", "1", "1"],
    ["1", "1", "0", "0"],
    ["0", "0", "0", "1"],
    ["0", "0", "1", "1"]
]



def numOfIslands(grid):
    island = 0
    disjointed_sets = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != '0':
                x = set()
                dfs(grid, r, c, x)
                island += 1
                disjointed_sets.append(x)
    return disjointed_sets


def dfs(grid, row, col, seen):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == "0":
        return
    seen.add((row,col))
    grid[row][col] = "0"
    dfs(grid, row-1, col, seen)
    dfs(grid, row, col-1, seen)
    dfs(grid,row+1,col, seen)
    dfs(grid,row, col+1, seen)



