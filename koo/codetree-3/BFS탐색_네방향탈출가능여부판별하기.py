import sys
from collections import deque
read = sys.stdin.readline

def sol():
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    n, m = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    def bfs():
        q = deque()
        q.append((0, 0))
        while q:
            x, y = q.popleft()
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < m and \
                    not visited[nx][ny] and graph[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = True
            if x == n - 1 and y == m - 1:
                return True
    print(1 if bfs() else 0)
    
sol()