import sys
from collections import deque
read = sys.stdin.readline
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def sol():
    n, m = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]
    
    def bfs():
        q = deque()
        if graph[0][0]:
            q.append((0, 0))
            visited[0][0] = 0
        else:
            return
        while q:
            x, y = q.popleft()
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < m and \
                    visited[nx][ny] < 0 and graph[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
    bfs()
    print(visited[n-1][m-1] if visited[n-1][m-1] != -1 else -1)


sol()