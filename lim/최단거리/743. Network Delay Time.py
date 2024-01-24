'''
정석 다익스트라 문제
'''


import sys
from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(lambda :defaultdict(int))
        for time in times:
            src, dst, cost = time
            graph[src][dst] = cost
        
        costs = [sys.maxsize] * (n+1)
        costs[k] = 0

        hq = [(0, k)]
        while len(hq):
            # 힙큐 속 노드에서 가장 비용이 낮은 노드 팝.
            cost, node = heapq.heappop(hq)
            # 최소 비용으로 갱신된 비용의 노드만 필요함. 그외에는 패스.
            if cost > costs[node]:
                continue
            for next_node in graph[node]:
                next_cost = cost + graph[node][next_node]
                # 이미 최소 갱신 됐다면 패스. 힙큐에 넣지 않음.
                if costs[next_node] <= next_cost: #  여기가 없으면 메모리 초과
                    continue
                # 간선 비용 갱신
                costs[next_node] = next_cost 
                # 갱신된 노드 힙큐에 추가
                heapq.heappush(hq, (next_cost, next_node))
        
        answer = max(costs[1:])
        if answer == sys.maxsize:
            return -1
        return answer

Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)