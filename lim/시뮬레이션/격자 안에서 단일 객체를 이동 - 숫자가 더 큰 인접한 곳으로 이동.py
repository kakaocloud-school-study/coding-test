import sys


def sol(n, s_r, s_c, grid):
    answer = []
    drs = [-1, 1, 0, 0]
    dcs = [0, 0, -1, 1]
    def move(r, c):
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if nr >= 0 and nr < n and nc >= 0 and nc < n and grid[r][c] < grid[nr][nc]:
                return nr, nc
        return None, None
    r, c = s_r, s_c
    while True:
        answer.append(grid[r][c])
        nr, nc = move(r, c)
        if nr == None:
            break
        r, c = nr, nc
    return answer

n, r, c = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for e in sol(n, r - 1, c - 1, grid):
    print(e, end=' ')