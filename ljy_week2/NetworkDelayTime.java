import java.util.*;

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        // 교재 풀이
        // 각 노드를 출발지 -> 도착지 형태의 그래프로 구현
        Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();
        for (int[] time : times) {
            graph.putIfAbsent(time[0], new HashMap<>());
            graph.get(time[0]).put(time[1],time[2]);
        }

        // 우선 순위 큐 생성
        // 정렬 기준은 도착지와 소요시간 기준
        Queue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(Map.Entry.comparingByValue());
        // Map.Entry를 이용하면 Map에 저장된 모든 key-value 쌍을 각각의 key-value를 갖고 있는 하나의 객체로 얻을 수 있다.

        // 도착지, 소요 시간을 큐에 삽입, 시작은 출발지, 소요시간은 0.
        pq.add(new AbstractMap.SimpleEntry<>(k, 0));
        // AbstractMap으로 골격을 제공 가능

        // (도착지, 소요 시간) 최종 결과를 저장하는 변수 선언
        Map<Integer, Integer> dist = new HashMap<>();

        // 큐에 값이 남아 있다면 없어질 때까지 반복
        while (!pq.isEmpty()) {
            // 소요시간이 가장 빠른 값 추출
            Map.Entry<Integer, Integer> cur = pq.poll();

            // 우선순위 큐의 항목이 Map.Entry이므로 순회 과정 없이
            // 간단히 getKey(), getValue()로 (도착지, 소요 시간)을 조회할 수 있다.
            int u = cur.getKey();
            int dist_u = cur.getValue();

            // u 지점 깍지의 소요 시간이 아직 계산되지 않았다면 처리 시작
            if(!dist.containsKey(u)) {
                // u 지점까지의 소요시간 (dist_u)을 결과 변수에 삽입
                dist.put(u, dist_u);
                // u 지점을 출발지로 한 경로가 있다면 처리 시작
                if (graph.containsKey(u)) {
                    // u 지점을 출발지로 한 모든 경로 순회
                    for (Map.Entry<Integer, Integer> v : graph.get(u).entrySet()) {
                        // u 지점까지의 소요 시간 (dist_u) + u 지점을 출발지로 한 도착지까지의 소요 시간
                        int alt = dist_u + v.getValue();
                        // 우선순위 큐에 (도착지, 소요시간)을 삽입
                        pq.add(new AbstractMap.SimpleEntry<>(v.getKey(), alt));
                    }
                }
            }
        }
        // 결과 변수가 노드의 수와 같다면 모든 노드의 소요 시간을 측정했고, 도달 가능하다는 의미.
        if (dist.size() == n) {
            return Collections.max(dist.values());
        }
        return -1;
    }
}