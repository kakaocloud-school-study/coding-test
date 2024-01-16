import sys
from typing import List
from collections import deque
read = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def sol(x: int, y: int) -> None:
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for d in directions:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m and \
                not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))

n, m = map(int, read().split())
res = 0
graph = [list(map(int, list(read().rstrip()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            sol(i, j)
            res += 1
print(res)