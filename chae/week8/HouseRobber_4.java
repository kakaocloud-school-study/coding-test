package codingTestStudy.week8;

public class HouseRobber_4 {
    public int rob(int[] nums) {
        int impossible= 0;
        int possible = 0;

        for(int num: nums) {
            int curRob =  possible + num;
            int curNoRob = Math.max(impossible, possible);

            impossible = curRob;
            possible = curNoRob;

        }

        return Math.max(possible, impossible);
    }

    public static void main(String[] args) {
        int[] num = {1,2,1,1};
        System.out.println(new HouseRobber_4().rob(num));
    }
}
