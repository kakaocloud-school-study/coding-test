from collections import defaultdict
import sys


def sol(n, edges):
    graph = [[sys.maxsize]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
        
    for src, dst, cost in edges:
        graph[src-1][dst-1] = min(graph[src-1][dst-1], cost)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    for i in range(n):
        for j in range(n):
            print(0 if graph[i][j] == sys.maxsize else graph[i][j], end=' ')
        print()

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
sol(n, edges)