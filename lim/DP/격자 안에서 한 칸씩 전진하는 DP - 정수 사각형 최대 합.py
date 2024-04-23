import sys


def sol(n, grid):
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, n):
        grid[i][0] += grid[i-1][0]

    for i in range(1, n):
        for j in range(1, n):
            grid[i][j] += max(grid[i-1][j], grid[i][j-1])
    return grid[n-1][n-1]

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, grid))