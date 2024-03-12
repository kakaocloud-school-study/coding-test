class Solution {
    public int maxSubArray(int[] nums) {
        // 교재 풀이 : 카데인 알고리즘
        int currentSum = 0;
        int bestSum = Integer.MIN_VALUE;
        for (int num : nums) {
            // 현재 값과 (누적된 값 + 현재 값) 중 더 큰 값을 저장
            currentSum = Math.max(num, currentSum + num);
            // 매번 최댓값을 계산하여 저장
            bestSum = Math.max(bestSum, currentSum);
        }
        return bestSum;
    }
}