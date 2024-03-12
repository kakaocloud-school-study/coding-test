class Solution {
    int[] numArr = new int[31];
    public int fib(int n) {
        if (n == 0) {
            return numArr[0];
        }
        if (n == 1) {
            if (numArr[1] == 0) {
                numArr[1] = 1;
            }
            return numArr[1];
        }
        if (numArr[n] == 0) {
            numArr[n] = fib(n - 1) + fib(n - 2);
        }
        return numArr[n];
    }
}