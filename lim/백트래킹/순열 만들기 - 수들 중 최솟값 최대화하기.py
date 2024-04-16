import sys


def sol(n):
    visited = set()
    def _sol(i, n):
        if i == n:
            return [[]]
        result = []
        for j in range(n):
            if j in visited:
                continue
            visited.add(j)
            for arr in _sol(i+1, n):
                result.append([j]+arr)
            visited.remove(j)
        return result
    return _sol(0, n)

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mins = []
for arr in sol(n):
    values = []
    for i, j in enumerate(arr):
        values.append(grid[i][j])
    mins.append(min(values))
print(max(mins))