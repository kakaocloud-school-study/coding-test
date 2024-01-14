class Solution {
    // 교재 풀이
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] pre: prerequisites) {
            map.putIfAbsent(pre[0], new ArrayList<>());
            map.get(pre[0]).add(pre[1]);
        }

        // 처리해ㅑ하는 노드를 저장하는 변수
        List<Integer> takes = new ArrayList<>();
        // 처리한 노드를 저장하는 변수
        List<Integer> taken = new ArrayList<>();
        // 완료해야하는 노드 순회
        for (Integer finish : map.keySet()) {
            if (!dfs(map, finish, takes, taken)) return false;
        }
        // 모든 코스에 문제가 없으므로 true 리턴
        return true;
    }

    public boolean dfs(Map<Integer, List<Integer>> map, Integer finish, List<Integer> takes, List<Integer> taken) {
        // 완료해야하는 노드가 처리해야하는 노드에 이미 포함되어있다면
        // 그래프가 순환 구조이므로 false 리턴
        if (takes.contains(finish)) return false;

        // 이미 처리한 노드라면
        if (taken.contains(finish)) return true;

        // 완료해야하는 코스에 값이 있다면
        if (map.containsKey(finish)) {
            // 처리해야하는 노드에 현재 완료해야하는 노드 추가
            takes.add(finish);
            // 처리해야하는 노드 순회
            for (Integer take : map.get(finish)) {
                // 재귀 dfs, 탐색 결과가 false라면 false를 리턴
                if (!dfs(map, take, takes, taken)) return false;
            }
            // 탐색 후에는 처리했으므로 노드 제거, 이미 처리한 노드 추가
            takes.remove(finish);
            taken.add(finish);
        }
        // 코스에 문제가 없으므로 true 리턴
        return true;
    }
}