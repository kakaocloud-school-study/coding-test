import sys

sys.setrecursionlimit(10**6)

def sol(n, m, k, grid):
    drs = [1, -1, 0, 0]
    dcs = [0, 0, 1, -1]
    visited = set()
    count = 0
    def out_range(r, c):
        return r < 0 or r >= n or c < 0 or c >= m
    def dfs(r, c):
        visited.add((r, c))
        count = 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc
            if out_range(nr, nc):
                continue
            if grid[nr][nc] <= k or (nr, nc) in visited:
                continue
            count += dfs(nr, nc)
        return count + 1
    for i in range(n):
        for j in range(m):
            if grid[i][j] <= k or (i, j) in visited:
                continue
            dfs(i, j)
            count += 1
    return count

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_count = 0
max_count_k = 1
for k in range(1, 101):
    count = sol(n, m, k, grid)
    if max_count < count:
        max_count = count
        max_count_k = k

print(max_count_k, max_count)