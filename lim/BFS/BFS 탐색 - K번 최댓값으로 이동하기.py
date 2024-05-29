from collections import deque
import sys

def sol(n, k, r, c, grid):
    drs = [1, -1, 0, 0]
    dcs = [0, 0, 1, -1]
    def out_range(r, c):
        return r < 0 or r >= n or c < 0 or c >= n
    def bfs(r, c):
        sr, sc = r, c
        max_r, max_c = r, c
        visited = set()
        visited.add((r, c))
        dq = deque([(r, c)])
        while len(dq):
            r, c = dq.popleft()
            for dr, dc in zip(drs, dcs):
                nr, nc = r+dr, c+dc
                if out_range(nr, nc):
                    continue
                if grid[nr][nc] >= grid[sr][sc] or (nr, nc) in visited:
                    continue
                dq.append((nr, nc))
                visited.add((nr, nc))
                if (max_r, max_c) == (sr, sc) or (grid[max_r][max_c], -max_r, -max_c) < (grid[nr][nc], -nr, -nc):
                    max_r, max_c = nr, nc
        return max_r, max_c
    
    for _ in range(k):
        nr, nc = bfs(r, c)
        if (nr, nc) == (r, c):
            break
        r, c = nr, nc
    return nr, nc

n, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
r, c = map(int, sys.stdin.readline().split())
r, c = sol(n, k, r-1, c-1, grid)
print(r+1, c+1)