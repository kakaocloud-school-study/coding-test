import sys
from collections import deque
from itertools import combinations
from typing import Tuple, List
read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def can_move(current_num: int, next_num: int, u: int, d: int):
    return u <= abs(current_num - next_num) <= d

def bfs(pos_comb: List[Tuple[int, int]]):
    print('pos_comb', pos_comb)
    q = deque()
    visited = [[False] * n for _ in range(n)]
    ret = 0
    for pos in pos_comb:
        q.append(pos)
        visited[pos[0]][pos[1]] = True
        ret += 1
    
    while q:
        x, y = q.popleft()
        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]
            if 0 <= nx < n and 0 <= ny < n and \
                not visited[nx][ny] and can_move(graph[x][y], graph[nx][ny], u, d):
                    visited[nx][ny] = True
                    ret += 1
                    q.append((nx, ny))
    print('ret', ret)
    print()
    return ret

n, k, u, d = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
poses = [(i, j) for i in range(n)
                for j in range(n)]
res = 0

for pos_comb in combinations(poses, k):
    res = max(res, bfs(pos_comb))

print(res)