from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        drs = [0, 0, -1, 1]
        dcs = [1, -1, 0, 0]
        m_len = len(grid)
        n_len = len(grid[0])

        visited = set()
        def can_go(r, c):
            return r >= 0 and c >= 0 and r < m_len and c < n_len and not (r, c) in visited and grid[r][c] == '1'

        def bfs(start_r, start_c):
            dq = deque([(start_r, start_c)])
            visited.add((start_r, start_c))
            while len(dq):
                r, c = dq.popleft()
                for dr, dc in zip(drs, dcs):
                    nr, nc = r + dr, c + dc
                    if can_go(nr, nc):
                        dq.append((nr, nc))
                        visited.add((nr, nc))

        total = 0
        for i in range(m_len):
            for j in range(n_len):
                if not can_go(i, j):
                    continue
                bfs(i, j)
                total += 1
        return total