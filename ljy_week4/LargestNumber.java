// 교재 풀이
class Solution {
    public boolean toSwap(int n1, int n2) {
        // 비교해 후자가 크면 스왑이 필요하므로 true 리턴
        return Long.parseLong(String.valueOf(n1) + n2) < Long.parseLong(String.valueOf(n2) + n1);
    }
    public String largestNumber(int[] nums) {
        int i = 1;
        while (i < nums.length) {
            int j = i;
            // j + [j - 1]이 더 클 경우 스왑 진행하면서 j 이동
            while (j > 0 && toSwap(nums[j - 1], nums[j])) {
                int temp = nums[j];
                nums[j] = nums[j-1];
                nums[j-1] = temp;
                // 정렬된 배열을 가리키는 포인터 j는 왼쪽으로 이동
            }
            // 정렬되지 않은 배열을 가리키는 포인터 i는 오른쪽으로 이동
            i++;
        }

        // 첫번째 값이 0이면 00같은 결과가 나오지 않도록 0을 최종 결과로 리턴
        if (nums[0] == 0) {
            return "0";
        } else {
            // 정수형 배열을 콤마나 대괄호, 공백은 정규식으로 제거하고 문자열로 결과 리턴
            return Arrays.toString(nums).replaceAll("\\[|\\]|,|\\s", "");
        }
    }
}