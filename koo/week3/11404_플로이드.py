import sys
read = sys.stdin.readline
INF = int(1e6)

n, m = int(read()), int(read())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()