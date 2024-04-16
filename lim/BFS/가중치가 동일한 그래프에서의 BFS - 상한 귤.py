from collections import defaultdict, deque
import sys


def sol(n, grid):
    def can_go(r, c):
        return 0<=r and r<n and 0<=c and c<n and grid[r][c] != 0
    def bfs(r, c):
        if grid[r][c] == 0:
            return -1
        visited = set([(r, c)])
        dq = deque([(r, c, 0)])
        while len(dq):
            r, c, depth = dq.popleft()
            if grid[r][c] == 2:
                return depth
            for dr, dc in ((0, 1),(1, 0),(0, -1),(-1, 0)):
                nr, nc = r+dr, c+dc
                if (nr, nc) in visited or not can_go(nr, nc):
                    continue
                visited.add((nr, nc))
                dq.append((nr, nc, depth+1))
        return -2
    n_grid = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            n_grid[i][j] = bfs(i, j)
    return n_grid

n, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for arr in sol(n, grid):
    for num in arr:
        print(num, end=' ')
    print()