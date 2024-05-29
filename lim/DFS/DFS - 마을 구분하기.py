import sys


def sol(n, grid):
    drs = [1, -1, 0, 0]
    dcs = [0, 0, 1, -1]
    visited = set()
    answer = []
    def out_range(r, c):
        return r < 0 or r >= n or c < 0 or c >= n
    def dfs(r, c):
        visited.add((r, c))
        count = 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc
            if out_range(nr, nc):
                continue
            if grid[nr][nc] != 1 or (nr, nc) in visited:
                continue
            count += dfs(nr, nc)
        return count + 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 1 or (i, j) in visited:
                continue
            count = dfs(i, j)
            if count == 0:
                continue
            answer.append(count)
    answer.sort()
    return answer

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sol(n, grid)
print(len(answer))
for num in answer:
    print(num)