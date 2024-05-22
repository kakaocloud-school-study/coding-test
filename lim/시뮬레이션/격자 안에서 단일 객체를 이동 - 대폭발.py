from copy import deepcopy
import sys


def sol(n, m, r, c):
    drs = [0, 1, 0, -1]
    dcs = [1, 0, -1, 0]
    grid = [[0]*n for _ in range(n)]
    grid[r][c] = 1

    def out_range(r, c):
        return r < 0 or r >= n or c < 0 or c >= n
    
    def bomb(grid, r, c, time):
        dist = 2 ** (time - 1)
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr*dist, c + dc*dist
            if out_range(nr, nc):
                continue
            grid[nr][nc] = 1

    def bombs(time):
        new_grid = deepcopy(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                bomb(new_grid, i, j, time)
        return new_grid
    
    for t in range(1, m+1):
        grid = bombs(t)
    
    count = 0
    for i in range(n):
        for j in range(n):
            count += grid[i][j]
    return count

n, m, r, c = map(int, sys.stdin.readline().split())

print(sol(n, m, r-1, c-1))