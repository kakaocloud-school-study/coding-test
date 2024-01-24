import java.util.*;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // 교재 풀이
        // 그래프 생성
        Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();

        for (int[] flight : flights) {
            graph.putIfAbsent(flight[0], new HashMap<>());
            graph.get(flight[0]).put(flight[1], flight[2]);
        }

        // 비용으로 정렬하는 우선순위 큐 생성
        Queue<List<Integer>> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.get(1)));
        pq.add(Arrays.asList(src, 0, 0));

        // 타임아웃 방지 경로 저장 맵
        Map<Integer, Integer> visited = new HashMap<>();

        while(!pq.isEmpty()) {
            List<Integer> cur = pq.poll();

            int u = cur.get(0);
            int dist_u = cur.get(1);
            int stops = cur.get(2);

            // 큐에서 추출한 값이 dst면 반환
            if (u == dst) return dist_u;

            visited.put(u, stops);
            if (stops <= k) {
                stops++; // 거친 stop + 1.
                // u에서 경로가 있다면
                if (graph.containsKey(u)) {
                    for (Map.Entry<Integer, Integer> v : graph.get(u).entrySet()) {
                        // 아직 계산한 경로가 아니거나 진행한 stops가 기존보다 작다면 큐에 삽입한다.
                        if (!visited.containsKey(v.getKey()) || stops < visited.get(v.getKey())){
                            pq.add(Arrays.asList(v.getKey(), v.getValue() + dist_u, stops));
                        }
                    }
                }
            }
        }
        // 도착지에 한번도 도착하지 못했다면 경로 없음 
        return -1;
    }
}