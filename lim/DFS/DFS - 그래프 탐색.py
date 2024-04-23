from collections import defaultdict, deque
import sys


def sol(n, m, grid):
    visited = set()
    def dfs(node):
        visited.add(node)
        for n_node in grid[node]:
            if n_node in visited:
                continue
            dfs(n_node)
    dfs(1)
    return len(visited) - 1    

n, m = map(int, sys.stdin.readline().split())
grid = defaultdict(set)
for node1, node2 in [map(int, sys.stdin.readline().split()) for _ in range(m)]:
    grid[node1].add(node2)
    grid[node2].add(node1)
print(sol(n, m, grid))