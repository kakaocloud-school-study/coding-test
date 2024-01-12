'''
오일러 경로의 변형
'''

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            src, dst = ticket
            heapq.heappush(graph[src], dst)
        
        def dfs(src):
            path = [src]
            while len(graph[src]):
                dst = heapq.heappop(graph[src])
                subpath = dfs(dst)
                if subpath[-1] == src:
                    path += subpath
                else:
                    end_path = subpath
            return path + end_path
        
        return dfs('JFK')