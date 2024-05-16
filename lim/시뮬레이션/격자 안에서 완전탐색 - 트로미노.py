import sys

def sol(n, m, grid):
    def cal(r, c):
        value = 0
        if r + 1 < n and c + 1 < m:
            value = max(value
                , grid[r][c]+grid[r+1][c]+grid[r][c+1]
                , grid[r][c]+grid[r+1][c]+grid[r+1][c+1]
                , grid[r][c]+grid[r][c+1]+grid[r+1][c+1]
                , grid[r+1][c]+grid[r][c+1]+grid[r+1][c+1]
            )
        if r + 2 < n:
            value = max(value, grid[r][c]+grid[r+1][c]+grid[r+2][c])
        if c + 2 < m:
            value = max(value, grid[r][c]+grid[r][c+1]+grid[r][c+2])
        return value
    answer = 0
    for i in range(n):
        for j in range(m):
            answer = max(answer, cal(i, j))
    return answer


n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, m, grid))