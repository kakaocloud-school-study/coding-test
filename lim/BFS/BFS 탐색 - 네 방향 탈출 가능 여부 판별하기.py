from collections import defaultdict, deque
import sys


def sol(n, m, grid):
    def can_go(r, c):
        return 0<=r and r<n and 0<=c and c<m and grid[r][c] != 0
    def bfs(r, c):
        visited = set([(r, c)])
        dq = deque([(r, c)])
        while len(dq):
            r, c = dq.popleft()
            if r == n - 1 and c == m - 1:
                return True
            for dr, dc in ((0, 1),(1, 0),(0, -1),(-1, 0)):
                nr, nc = r+dr, c+dc
                if (nr, nc) in visited or not can_go(nr, nc):
                    continue
                visited.add((nr, nc))
                dq.append((nr, nc))
        return False
    return bfs(0,0)

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(int(sol(n, m, grid)))