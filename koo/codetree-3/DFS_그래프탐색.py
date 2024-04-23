import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
checker = set()
res = 0

for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

checker.add(1)
visited[1] = True
while checker:
    x = checker.pop()
    for elem in graph[x]:
        if not visited[elem]:
            visited[elem] = True
            checker.add(elem)
            res += 1

print(res)