import heapq
import json

# network_delay_time 함수는 네트워크 딜레이 타임을 계산함.
# network_delay_time 함수는 전체 프로그램의 진입점.
def network_delay_time(times, N, K): #times: []로 구성되는 출발지 도착지 소요시간, n은 노드수, k는 출발지.
    # N+1개의 빈배열을 만들어 graph에 할당한다. 인덱스 0을 사용하지 않으려고 +1을 해준다.
    graph = [[] for _ in range(N + 1)] #루프 내에서 변수를 사용하지 않을때 언더바(_)를 씀.

    # 주어진 간선 정보(times)를 순회한다. times는 리스트고 u,v,w는 변수다.
    # graph의 각 인덱스가 하나의 노드를 대표함.'u'번째 요소에 (v,w)튜플을 추가함.
    for u, v, w in times:
        graph[u].append((v, w))


    # 최단 경로를 저장할 리스트를 무한대 값으로 초기화한다.
    # 코드 실행 전에는 모든 노드까지의 거리를 모르는 상태이기 때문에 '무한대'로 초기화해주는게 일반적이다.
    #(N+1)을 곱해주는 것은 무한대로 초기화 한 배열을 N+1만큼 생성한다는 의미다.
    distance = [float('inf')] * (N + 1)

    # 다익스트라 알고리즘을 구현하는 내부 함수. 함수선언은 def로 함.
    # dijkstra 함수는 network_delay_time 함수 내에서만 호출할 수 있다.
    def dijkstra(start):
        q = [(0, start)]  # 시작 노드와 거리(0)를 튜플로 큐에 넣음.
        distance[start] = 0  # 시작 노드의 최단 거리를 0으로 설정함.
        while q:  # 큐가 빌 때까지 반복합니다.

            # 힙에서 거리가 가장 짧은 노드를 꺼냄.(heapq모듈이 최소힙을 구현!)
            # 힙의 루트(힙의 첫번째요소)는 항상 힙 내에서 가장 작은 값.
            # 'q'힙에는 (거리, 노드 번호)가 추가되어있고, '거리'값을 기준으로 정렬됨.
            dist, now = heapq.heappop(q)

            #이미 더 짧은 경로를 통해 now에 도달했는지 확인하고자 조건문 씀.
            if distance[now] < dist:
                continue  # 이미 처리된 노드는 패스함.

            # 현재 노드와 인접한 노드들을 순회한다.
            for v, w in graph[now]:

                # 현재 노드를 거쳐 인접 노드로 가는 비용을 계산합니다.
                cost = dist + w

                # 계산된 비용이 기존의 최단 거리보다 작으면 업데이트함.
                if cost < distance[v]:
                    distance[v] = cost
                    # 'q'힙에 (cost,v) 튜플을 추가한다.
                    heapq.heappush(q, (cost, v))

    dijkstra(K)  # 시작 노드 K에서 다익스트라 알고리즘을 실행합니다.

    # 모든 노드까지의 최대 딜레이 시간을 계산함.
    #리스트[시작인덱스:끝인덱스] => distance[1:]은 리스트 두번째부터 마지막까지 선택한다는 뜻.
    #왜? 0번 인덱스를 사용하지 않고 1번인덱스=1번노드이기 때문!
    max_distance = max(distance[1:])

    # 최대 딜레이 시간이 무한대가 아니면 해당 값을(노드에 도달하면), 그렇지 않으면 -1을 반환한다.
    # 파이썬의 조건부 표현식 : X if 조건 else Y
    # 조건이 참이면 x를 반환하고 아니면 Y를 반환한다.
    return max_distance if max_distance < float('inf') else -1


# 사용자 입력을 받는 부분
times = json.loads(input()) #리스트 형식은 JSON형식으로 변환할 필요없음.

N = int(input())  # 노드의 개수를 입력받습니다.
K = int(input())

# 함수를 호출하여 결과를 계산하고 출력합니다.
delay_time = network_delay_time(times, N, K)
print(delay_time) # {}괄호안에 변수나 표현식을 넣어서 값을 출력함.