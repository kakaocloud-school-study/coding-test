import java.util.*;

class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        // 진수 변환
        String str = Integer.toString(n, k);
        
        // 0으로 split
        String[] arr = str.split("0+");
        
        // 순회하며 소수를 찾음
        for (String s : arr) {
            if (s.equals("1")) continue;
            if (isPrime(s)) answer++;
        }
        
        return answer;
    }
    
    // 소수인지 확인
    private boolean isPrime(String s) {
        long num = Long.parseLong(s);
        
        for (int i = 2; i < (long) Math.sqrt(num) + 1; i++) {
            if (num % (long)i == 0L) return false;
        }
        
        return true;
    }
}