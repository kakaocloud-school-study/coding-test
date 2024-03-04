class Solution {
    public int majorityElement(int[] nums) {
        // 개수 정리할 맵
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.putIfAbsent(num, 0);
            map.put(num, map.get(num) + 1);
        }

        // 개수대로 정리하기
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            pq.add(new int[]{entry.getKey(), entry.getValue()});
        };

        return pq.poll()[0];
    }
}