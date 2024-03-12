import java.util.*;

class Solution {
    public int solution(int[] money) {
        return Math.max(
            rob(Arrays.copyOfRange(money, 0, money.length - 1)),
                rob(Arrays.copyOfRange(money, 1, money.length)));
    }
    
    private int rob(int[] money) {
        if (money.length == 1) return money[0];
        int[] dp = new int[money.length];
        dp[0] = money[0];
        dp[1] = Math.max(money[0], money[1]);
        for (int i = 2; i < money.length; i++) {
            dp[i] = Math.max(dp[i-1], dp[i-2] + money[i]);
        }
        
        return dp[money.length - 1];
    }
}