import sys
from queue import deque
read = sys.stdin.readline

def sol() -> int:
    n = int(read())
    graph = [[] for _ in range(n + 1)]
    q = deque()
    dist = [0] * (n + 1)
    s, e = map(int, read().split())
    m = int(read())
    for _ in range(m):
        x, y = map(int, read().split())
        graph[x].append(y)
        graph[y].append(x)

    
    q.append(s)
    while q:
        v = q.popleft()
        for w in graph[v]:
            if dist[w] == 0 and w != s:
                dist[w] = dist[v] + 1
                q.append(w)
    
    
    return dist[e] if dist[e] != 0 else -1

print(sol())