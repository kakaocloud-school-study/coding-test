import sys
from collections import deque
read = sys.stdin.readline

def sol():
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    n = int(read())
    graph = [list(map(int, read().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    explosion, max_block_size = 0, 0
    
    def bfs(i: int, j: int):
        block = graph[i][j]
        size = 1
        q = deque()
        q.append((i, j))
        visited[i][j] = True
        
        while q:
            x, y = q.popleft()
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < n and \
                    not visited[nx][ny] and graph[nx][ny] == block:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        size += 1
        nonlocal max_block_size
        max_block_size = max(max_block_size, size)
        return True if size >= 4 else False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j):
                    explosion += 1
    print(explosion, max_block_size)

sol()
                        
                