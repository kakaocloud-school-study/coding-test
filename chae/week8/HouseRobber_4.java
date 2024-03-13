package codingTestStudy.week8;

public class HouseRobber_4 {
    public int rob(int[] nums) {
        if (nums.length==1){
            return nums[0];
        } else if (nums.length==2){
            return Math.max(nums[0],nums[1]);
        }
        int[] array = new int[nums.length];
        int max = nums[0];
        int previousMax = nums[0];
        for (int i = 2; i<nums.length; i++){
             array[i] = Math.max(nums[i]+previousMax, nums[i]);
             previousMax = Math.max(array[i-1],previousMax);
             max = Math.max(array[i],max);
        }
        return Math.max(max,nums[1]);
    }

    public static void main(String[] args) {
        int[] num = {1,2,1,1};
        System.out.println(new HouseRobber_4().rob(num));
    }
}
