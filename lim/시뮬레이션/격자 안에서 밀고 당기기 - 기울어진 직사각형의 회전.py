from collections import deque
import sys

def sol(n, grid, r, c, moves, direction):
    drs = [-1, -1, 1, 1]
    dcs = [1, -1, -1, 1]
    q = deque([])
    o_r, o_c = r, c
    for dr, dc, move in zip(drs, dcs, moves):
        for _ in range(move):
            q.append(grid[r][c])
            r, c = r+dr, c+dc
    q.rotate({0:1, 1:-1}[direction])
    r, c = o_r, o_c
    for dr, dc, move in zip(drs, dcs, moves):
        for _ in range(move):
            grid[r][c] = q.popleft()
            r, c = r+dr, c+dc


n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
r, c, *moves, direction = map(int, sys.stdin.readline().split())

sol(n, grid, r-1, c-1, moves, direction)
for arr in grid:
    for num in arr:
        print(num, end=' ')
    print()