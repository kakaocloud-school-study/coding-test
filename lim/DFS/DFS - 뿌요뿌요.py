from collections import defaultdict, deque
import sys


def sol(n, grid):
    visited = set()
    def can_go(r, c):
        return 0<=r and r<n and 0<=c and c<n
    def dfs(r, c):
        visited.add((r, c))
        count = 1
        for dr, dc in ((0, 1),(0, -1),(1, 0),(-1, 0)):
            nr, nc = r+dr, c+dc
            if (nr, nc) in visited or (not can_go(nr, nc)) or grid[r][c] != grid[nr][nc]:
                continue
            count += dfs(nr, nc)
        return count
    
    max_size = 0
    bomb = 0
    for i in range(n):
        for j in range(n):
            count = dfs(i, j)
            if count > max_size:
                max_size = count
            if count < 4:
                continue
            bomb += 1
    return bomb, max_size

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print('{} {}'.format(*sol(n, grid)))