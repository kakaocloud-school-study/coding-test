import sys


def sol(n, m, t, grid, count_grid):
    count = 0

    drs = [-1, 1, 0, 0]
    dcs = [0, 0, -1, 1]
    def move(new_count_grid, r, c):
        max_r, max_c = None, None
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                if max_r == None:
                    max_r, max_c = nr, nc
                elif grid[max_r][max_c] < grid[nr][nc]:
                    max_r, max_c = nr, nc
        new_count_grid[max_r][max_c] += 1

    def move_all():
        new_count_grid = [[0 for __ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if count_grid[i][j] == 0:
                    continue
                move(new_count_grid, i, j)
        return new_count_grid
    
    def clean():
        for i in range(n):
            for j in range(n):
                if count_grid[i][j] > 1:
                    count_grid[i][j] = 0
    
    while t:
        t -= 1
        count_grid = move_all()
        clean()
    
    for i in range(n):
        for j in range(n):
            if count_grid[i][j] == 0:
                continue
            count += 1
    return count


n, m, t = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count_grid = [[0 for __ in range(n)] for _ in range(n)]
for i in range(m):
    r, c = map(int, sys.stdin.readline().split())
    count_grid[r-1][c-1] = 1

print(sol(n, m, t, grid, count_grid))