import sys
from collections import deque
read = sys.stdin.readline

'''
0 : 빈 칸
1 : 귤
2 : 상한 귤
'''
def sol():
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    n, k = map(int, read().split())
    graph = [list(map(int, read().split())) for i in range(n)]
    visited = [[-2] * n for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 0
            elif graph[i][j] == 0:
                visited[i][j] = -1
    
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n and \
                visited[nx][ny] == -2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    
    for row in visited:
        print(*row)

sol()