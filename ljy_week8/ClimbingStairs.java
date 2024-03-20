class Solution {
    int[] mem = new int[46];
    public int climbStairs(int n) {
        if (n == 1) {
            if (mem[1] == 0) {
                mem[1] = 1;
            }
            return mem[1];
        };
        if (n == 2) {
            if (mem[2] == 0) {
                mem[2] = 2;
            }
            return mem[2];
        }
        if (mem[n] == 0) {
            mem[n] = climbStairs(n - 1) + climbStairs(n - 2);
        }
        return mem[n];
    }
}
