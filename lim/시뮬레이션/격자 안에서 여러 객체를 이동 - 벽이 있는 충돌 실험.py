import sys


def sol(n, grid):
    count = 0

    drs = [-1, 0, 1, 0]
    dcs = [0, -1, 0, 1]
    def move(new_grid, r, c, direction):
        nr, nc = r+drs[direction], c+dcs[direction]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            direction = (direction + 2) % 4
            if new_grid[r][c] == None:
                new_grid[r][c] = direction
            else:
                new_grid[r][c] = 5
        else:
            if new_grid[nr][nc] == None:
                new_grid[nr][nc] = direction
            else:
                new_grid[nr][nc] = 5

    def move_all():
        new_grid = [[None for __ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == None:
                    continue
                move(new_grid, i, j, grid[i][j])
        return new_grid
    
    def clean():
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 5:
                    grid[i][j] = None
    t = 2*n
    while t:
        t -= 1
        grid = move_all()
        clean()
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == None:
                continue
            count += 1
    return count

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    grid = [[None for __ in range(n)] for _ in range(n)]
    for _ in range(m):
        r, c, direction = sys.stdin.readline().split()
        r, c, direction = int(r), int(c), {'U':0,'L':1,'D':2,'R':3}[direction]
        grid[r-1][c-1] = direction

    print(sol(n, grid)) 