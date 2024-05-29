from collections import deque
import sys

def sol(n, h, m, grid):
    drs = [1, -1, 0, 0]
    dcs = [0, 0, 1, -1]
    def out_range(r, c):
        return r < 0 or r >= n or c < 0 or c >= n
    def bfs(r, c):
        WALL = 1
        HUMAN = 2
        SAFE = 3
        if grid[r][c] != HUMAN:
            return 0
        
        visited = set()
        visited.add((r, c))
        dq = deque([(r, c, 0)])
        while len(dq):
            r, c, depth = dq.popleft()
            if grid[r][c] == SAFE:
                return depth
            for dr, dc in zip(drs, dcs):
                nr, nc = r+dr, c+dc
                if out_range(nr, nc):
                    continue
                if (nr, nc) in visited:
                    continue
                if grid[nr][nc] == WALL:
                    continue
                dq.append((nr, nc, depth + 1))
                visited.add((nr, nc))
        return -1
    
    for i in range(n):
        for j in range(n):
            print(bfs(i, j), end=' ')
        print()

n, h, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sol(n, h, m, grid)