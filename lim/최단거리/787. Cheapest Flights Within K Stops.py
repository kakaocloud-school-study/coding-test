'''
다익스트라 확장
(다익스트라 ElogV 시간) * (k개 비교 시간)
대략 (n^3) * logn = 1_000_000 * c

백준에 N번 지점에 K번째 빠른 경로 찾는 문제와 유사함
'''
from collections import defaultdict
import heapq
import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(lambda :defaultdict(int))
        for flight in flights:
            s, d, cost = flight
            graph[s][d] = cost
        
        costs = [[sys.maxsize] * (k+2) for _ in range(n)]
        costs[src][0] = 0

        hq = [(0, 0, src)]
        while len(hq):
            # 힙큐 속 노드에서 가장 비용이 낮은 노드 팝.
            cost, depth, node = heapq.heappop(hq)
            # 최소 비용으로 갱신된 비용의 노드만 필요함. 그외에는 패스.
            if cost > costs[node][depth]:
                continue
            if depth > k: # k+1 이상 경유지는 안 봐도 됨.
                continue
            for next_node in graph[node]:
                next_depth = depth + 1
                next_cost = cost + graph[node][next_node]

                # 이미 최소 갱신 됐다면 패스. 힙큐에 넣지 않음.
                if costs[next_node][next_depth] <= next_cost: #  여기가 없으면 메모리 초과
                    continue
                # 간선 비용 갱신
                costs[next_node][next_depth] = next_cost
                # 갱신된 노드 힙큐에 추가
                heapq.heappush(hq, (next_cost, next_depth, next_node))
        
        answer = min(costs[dst])
        if answer == sys.maxsize:
            return -1
        return answer
    
Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1)