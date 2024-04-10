'''
400 * 400 * 400 = 64_000_000
'''

import sys


def sol(grid, n, m):
    def check(r1, c1, r2, c2):
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if grid[i][j] <= 0:
                    return False
        return True
    max_count = -1
    for i1 in range(0, n):
        for j1 in range(0, m):
            for i2 in range(i1, n):
                for j2 in range(j1, m):
                    if check(i1, j1, i2, j2):
                        max_count = max(max_count, (i2 - i1 + 1) * (j2 - j1 + 1))
    return max_count

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(grid, n, m))