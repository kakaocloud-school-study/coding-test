from collections import defaultdict, deque
import sys


def sol(n, m, grid):
    visited = set()
    def can_go(r, c):
        return 0<=r and r<n and 0<=c and c<m and grid[r][c] != 0
    def dfs(r, c):
        if r == n - 1 and c == m - 1:
            return True
        visited.add((r, c))
        found = False
        for dr, dc in ((0, 1),(1, 0)):
            nr, nc = r+dr, c+dc
            if (nr, nc) in visited or not can_go(nr, nc):
                continue
            found |= dfs(nr, nc)
        return found
    return dfs(0,0)

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
print(int(sol(n, m, grid)))