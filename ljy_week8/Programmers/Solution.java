package ljy_week8.Programmers;

class Solution {
    public String solution(String number, int k) {
        // 검색 풀이
        String answer = "";
        int ansLen = number.length() - k; // 정답의 길이
        int idx = 0;
        int remem = 0;
        // 일정 범위 안에서 찾는다.
        // 예를 들어 4자리 수에 k=2라면 앞의 3자리에서 하나를 찾는다.
        for (int i = answer.length(); i < ansLen; i++) {
            char max = '0';
            for (int j = idx; j < number.length() - ansLen + answer.length() + 1 ; j++) {
                
                if (number.charAt(j) == '9'){
                    max = '9';
                    remem = j+1;
                    break;
                }
                if (max < number.charAt(j)) {
                    max = number.charAt(j);
                    remem = j+1;
                }
            }
            idx = remem;
            answer += max;
        }
        return answer;
    }
}
