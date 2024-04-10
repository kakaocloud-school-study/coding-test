import sys


def sol(n, grid):
    def has_removed(r, c, b_r, b_c):
        dist = grid[b_r][b_c]
        return (abs(r - b_r) < dist and c == b_c) or (abs(c - b_c) < dist and r == b_r)
    def bomb(r, c):
        new_grid = [[0] * n for _ in range(n)]
        for j in range(n):
            new_i = 0
            for i in range(n - 1, -1, -1):
                if has_removed(i, j, r, c):
                    continue
                new_grid[new_i][j] = grid[i][j]
                new_i += 1
        return new_grid
    def count_couple(new_grid):
        count = 0
        for i in range(0, n):
            for j in range(0, n):
                if i + 1 < n and new_grid[i][j] != 0 and new_grid[i][j] == new_grid[i+1][j]:
                    count += 1
                if j + 1 < n and new_grid[i][j] != 0 and new_grid[i][j] == new_grid[i][j+1]:
                    count += 1
        return count

    max_count = 0
    for i in range(0, n):
        for j in range(0, n):
            new_grid = bomb(i, j)
            max_count = max(max_count, count_couple(new_grid))
    return max_count

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, grid))