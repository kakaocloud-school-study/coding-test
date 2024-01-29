import sys
from queue import deque
read = sys.stdin.readline



def sol() -> int:
    n, m = int(read()), int(read())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)
    q = deque()
    res = 0
    
    for _ in range(m):
        s, e = map(int, read().split())
        graph[s].append(e)
        graph[e].append(s)
    
    q.append(1)
    visited[1] = True
    while q:
        x = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                res += 1
    return res
                
print(sol())