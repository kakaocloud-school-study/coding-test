package codingTestStudy.week8;

public class MaximumSubarray_2 {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int[] array = new int[nums.length];
        array[0] = nums[0];
        for(int i=1; i<nums.length; i++){
            int n = array[i-1]+nums[i];
            int nm = Math.max(n,nums[i]);
            if (nm>max){
                max =nm;
            }
            array[i]=nm;
        }
        return max;
    }
}
