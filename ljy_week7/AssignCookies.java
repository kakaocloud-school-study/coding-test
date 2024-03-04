class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // 우선순위 큐로 정렬
        PriorityQueue<Integer> gpq = new PriorityQueue<>((a, b) -> b - a);
        PriorityQueue<Integer> spq = new PriorityQueue<>((a, b) -> b - a);
        for (int i : g) {
            gpq.add(i);
        }
        for (int i : s) {
            spq.add(i);
        }

        int count = 0; // 만족한 수

        // 한쪽이 빌 때까지 gpq를 기준으로 순회
        while (!spq.isEmpty() && !gpq.isEmpty()) {
            int child = gpq.poll();
            int cookie = spq.poll();

            if (child <= cookie) {
                count++; // 만족하면 +1
            } else {
                spq.add(cookie); // 만족하지 못하면 cookie는 다시 넣어둠
            }
        }

        return count;
    }
}