import sys


def sol(grid):
    def count_33(r, c):
        s_r = max(0, r-1)
        s_c = max(0, c-1)
        e_r = min(len(grid) - 1, r + 1)
        e_c = min(len(grid) - 1, c + 1)
        count = 0
        for i in range(s_r, e_r + 1):
            for j in range(s_c, e_c + 1):
                count += grid[i][j]
        return count
    max_count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            max_count = max(max_count, count_33(i, j))
    return max_count

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(grid))