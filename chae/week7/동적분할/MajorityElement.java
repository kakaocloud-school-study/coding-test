package codingTestStudy.week7.동적분할;

public class MajorityElement {
    public int majorityElement(int[] nums) {
        int count = 0;
        int result = 0;
        for (int num : nums){
            if (count == 0){
                result = num;
            }
            count += (num == result)?1:-1;
        }
        return result;
    }
}
