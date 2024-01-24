import heapq
import json

# Time Limit Exceeded
# 더 최적경로를 찾는 조건을 추가해줘야할듯
# 현재 문제점 : 동일 노드를 중복방문함.
# 개선점 : 동일 노드를 중복방문하지 않는다. 이미 탐색조건을 만족했다면 탐색을 중단한다.
# 개선한 부분
# 1. 최소비용 저장 딕셔너리 만들음 --> 테스트케이스 통과못함
# 2. 경유 횟수 추적(더 비싼 경로여도 더 적은 경유를 선택)

def findCeapestPrice(n,flights,src,dst,K):
    #flights를 입력받아 [[출발지(u), 도착지(v), 비용(w)]]을 저장할 graph 딕셔너리를 만들어준다.
    #파이썬에서 딕셔너리는 java의 hashMap과 비슷하다.(key와 value로 저장)
    graph = {i:[] for i in range(n)}

    #flights 리스트를 순회한다.
    #graph딕셔너리의 u키에 해당하는 리스트에 튜플(v,w)을 추가.
    for u,v,w in flights:
        graph[u].append((v,w))

    #각 노드에 도달하기 위한 최소 비용과 경유횟수를 저장하는 딕셔너리
    #실제 경유횟수에 출발지와 도착지를 고려해야하니 K+2를 해줌.
    minCost = {(i, k): float('inf') for i in range(n) for k in range(K+2)}
    minCost[src,K+1] = 0


    #(비용,현재 노드,남은 경유지 수)
    queue = [(0,src,K+1)]

    #큐가 빌 때까지 반복
    while queue:
        price, node, stop = heapq.heappop(queue)
        #목적지에 도달하면 비용을 리턴한다.
        if node == dst:
            return price

        #남은 경유 횟수 확인
        if stop > 0:
            # graph딕셔너리의 node에서 출발하는 모든 항공편을 순회한다.
            for v, w in graph[node]:
                nextPrice = price + w
                #현재 경로가 이 노드에 도달하기 위한 기존 최소비용(minCost[v])보다 저렴하면 큐에 추가함.
                #또, 현재 경로가 이전 계산된 경로보다 비용이 더 낮거나, 같은 비용으로 더 적은 경유라면, 업데이트해줌.
                if nextPrice < minCost[v,stop-1]:
                    minCost[v, stop-1] = nextPrice
                    heapq.heappush(queue,(nextPrice, v, stop-1))

    #목적지 도달 못한 경우, -1 반환
    return -1

#입력 받는 부분
n = int(input())
flights = json.loads(input())
src = int(input())
dst = int(input())
K = int(input())

print(findCeapestPrice(n, flights, src, dst, K))
