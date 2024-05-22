import heapq
import sys


def sol(n, t, k, grid):
    count = 0

    drs = [-1, 0, 1, 0]
    dcs = [0, -1, 0, 1]
    def next_pos(r, c, v, d):
        nr, nc = r+drs[d]*v, c+dcs[d]*v
        nr = ((nr + 2*n-2) %(2*n-2))
        nc = ((nc + 2*n-2) %(2*n-2))
        if nr >= n:
            nr = 2*n-2 - nr
            d = (d + 2) % 4
        if nc >= n:
            nc = 2*n-2 - nc
            d = (d + 2) % 4
        return nr, nc, d
    def move(new_grid, r, c, v, idx, d):
        nr, nc, nd = next_pos(r, c, v, d)

        heapq.heappush(new_grid[nr][nc], (v, idx, nd))
        if len(new_grid[nr][nc]) > k:
            heapq.heappop(new_grid[nr][nc])

    def move_all():
        new_grid = [[list() for __ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if len(grid[i][j]) == 0:
                    continue
                for v, idx, d in grid[i][j]:
                    move(new_grid, i, j, v, idx, d)
        return new_grid
    
    while t:
        t -= 1
        grid = move_all()
    
    for i in range(n):
        for j in range(n):
            count += len(grid[i][j])
    return count

n, m, t, k = map(int, sys.stdin.readline().split())
grid = [[list() for __ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, d, v = sys.stdin.readline().split()
    r, c, d, v = int(r), int(c), {'U':0,'L':1,'D':2,'R':3}[d], int(v)
    grid[r-1][c-1].append((v, i, d))

print(sol(n, t, k, grid)) 