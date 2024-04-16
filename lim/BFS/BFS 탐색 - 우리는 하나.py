from collections import defaultdict, deque
import sys


def sol(n, k, u, d, grid):
    visited = set()
    def can_go(r, c):
        return 0<=r and r<n and 0<=c and c<n
    def in_range(r, c, nr, nc):
        diff = abs(grid[r][c] - grid[nr][nc])
        return u <= diff and diff <= d
    def bfs(r, c):
        visited.add((r, c))
        dq = deque([(r, c)])
        count = 0
        while len(dq):
            r, c = dq.popleft()
            count += 1
            for dr, dc in ((0, 1),(1, 0),(0, -1),(-1, 0)):
                nr, nc = r+dr, c+dc
                if (nr, nc) in visited or not can_go(nr, nc) or not in_range(r, c, nr, nc):
                    continue
                visited.add((nr, nc))
                dq.append((nr, nc))
        return count
    
    counts = []
    for i in range(n):
        for j in range(n):
            if (i, j) in visited:
                continue
            counts.append(bfs(i, j))
    return sum(sorted(counts, reverse=True)[:k])

n, k, u, d = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(int(sol(n, k, u, d, grid)))