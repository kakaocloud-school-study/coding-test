from collections import deque
import sys

def sol(n, m, grid):
    drs = [1, -1, 0, 0]
    dcs = [0, 0, 1, -1]
    def out_range(r, c):
        return r < 0 or r >= n or c < 0 or c >= m
    def bfs(r, c):
        count = 0
        visited = set()
        visited.add((r, c))
        dq = deque([(r, c)])
        while len(dq):
            r, c = dq.popleft()
            if grid[r][c] == 1:
                grid[r][c] = 0
                count += 1
                continue
            for dr, dc in zip(drs, dcs):
                nr, nc = r+dr, c+dc
                if out_range(nr, nc):
                    continue
                if (nr, nc) in visited:
                    continue
                dq.append((nr, nc))
                visited.add((nr, nc))
        return count
    
    time = 0
    last_count = 0
    while True:
        count = bfs(0, 0)
        if count == 0:
            break
        last_count = count
        time += 1
    return time, last_count

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
t, count = sol(n, m, grid)
print(t, count)