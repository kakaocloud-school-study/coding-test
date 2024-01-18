import sys
from collections import defaultdict, deque


def sol(n, src, dst, edges):
    graph = defaultdict(set)
    for edge in edges:
        node1, node2 = edge
        graph[node1].add(node2)
        graph[node2].add(node1)
    
    def bfs(node):
        visited = set([node])
        dq = deque([(node, 0)])
        while len(dq):
            node, depth = dq.popleft()
            for next_node in graph[node]:
                if next_node == dst:
                    return depth + 1
                if next_node not in visited:
                    visited.add(next_node)
                    dq.append((next_node, depth+1))
        return -1
    print(bfs(src))


n = int(sys.stdin.readline())
x, y = sys.stdin.readline().split()
m = int(sys.stdin.readline())
edges = [sys.stdin.readline().split() for _ in range(m)]
sol(n, x, y, edges)

