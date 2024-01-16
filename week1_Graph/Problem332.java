class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        // 교재 풀이
        Map<String, PriorityQueue<String>> map = new HashMap<>();

        for (List<String> ticket : tickets) {
            map.putIfAbsent(ticket.get(0), new PriorityQueue<>());
            map.get(ticket.get(0)).add(ticket.get(1));
        }

        List<String> answer = new LinkedList<>();
        Deque<String> stack = new ArrayDeque<>();

        // 출발지 삽입
        stack.push("JFK");
        while(!stack.isEmpty()) {
            // 스택에서 추출될 값을 출발지로 한 도착지 처리
            while(map.containsKey(stack.getFirst()) && !map.get(stack.getFirst()).isEmpty()) {
                stack.push(map.get(stack.getFirst()).poll());
            }

            // 위 반복문이 모두 실행된 이후에는 스택에서 값이 하나씩 추출되어 정답으로 구성된다.
            answer.add(0, stack.pop());
        }

        return new ArrayList<>(answer);
    }
}