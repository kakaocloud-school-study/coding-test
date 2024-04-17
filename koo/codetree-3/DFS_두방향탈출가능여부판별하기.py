import sys
read = sys.stdin.readline

def sol():
    directions = [(1, 0), (0, 1)]
    n, m = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    def dfs():
        stk = []
        stk.append((0, 0))
        visited[0][0] = True
        while stk:
            x, y = stk.pop()
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < m and \
                    not visited[nx][ny] and graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        stk.append((nx, ny))
    dfs()
    print(1 if visited[n-1][m-1] else 0)
    
sol()