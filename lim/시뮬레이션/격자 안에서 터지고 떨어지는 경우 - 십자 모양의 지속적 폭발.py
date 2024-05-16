import sys


def sol(n, grid, cols):
    def has_removed(r, c, b_r, b_c):
        dist = grid[b_r][b_c]
        return (abs(r - b_r) < dist and c == b_c) or (abs(c - b_c) < dist and r == b_r)
    def bomb(r, c):
        new_grid = [[0] * n for _ in range(n)]
        for j in range(n):
            new_i = n-1
            for i in range(n - 1, -1, -1):
                if has_removed(i, j, r, c):
                    continue
                new_grid[new_i][j] = grid[i][j]
                new_i -= 1
        return new_grid
    def find_nonzero(col):
        for i in range(n):
            if grid[i][col] != 0:
                return i
        return n

    for j in cols:
        i = find_nonzero(j)
        if i == n:
            continue
        grid = bomb(i, j)
    return grid

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cols = [int(sys.stdin.readline())-1 for _ in range(m)]

grid = sol(n, grid, cols)
for arr in grid:
    for num in arr:
        print(num, end=' ')
    print()