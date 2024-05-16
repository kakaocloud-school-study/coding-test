from collections import deque
import sys

def sol(n, m, queries, grid):
    def check(idx1, idx2):
        if idx1 >= n or idx1 < 0 or idx2 >= n or idx2 < 0:
            return False
        for j in range(m):
            if grid[idx1][j] == grid[idx2][j]:
                return True
        return False
    def shift(idx, lr, ud):
        grid[idx].rotate(lr)
        if ud in (0, -1) and check(idx, idx-1):
            shift(idx-1, -lr, -1)
        if ud in (0, 1) and check(idx, idx+1):
            shift(idx+1, -lr, 1)
            
    for idx, lr in queries:
        shift(idx, lr, 0)


n, m, q = map(int, sys.stdin.readline().split())
grid = [deque(map(int, sys.stdin.readline().split())) for _ in range(n)]
queries = list(map(lambda query:[int(query[0])-1, {'L':1,'R':-1}[query[1]]], [sys.stdin.readline().split() for _ in range(q)]))

sol(n, m, queries, grid)

for arr in grid:
    for num in arr:
        print(num, end=' ')
    print()