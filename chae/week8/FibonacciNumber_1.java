package codingTestStudy.week8;

public class FibonacciNumber_1 {
    public int fib(int n) {
        int[] array = new int[31];
        array[1] =1;
        for (int i=2; i<=n; i++){
            array[i] = array[i-1]+array[i-2];
        }
        return array[n];
    }
}
