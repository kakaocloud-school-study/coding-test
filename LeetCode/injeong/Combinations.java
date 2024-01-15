package LeetCode.injeong;

import java.util.*;
public class Combinations {
/*문제해결로직
* 1. 결과 저장할 리스트 초기화
* 2. DFS 함수 정의
* 3. DFS 실행
* 4. 결과 반환
* main에서 combine 호출 -> dfs 호출 -> result return -> main에서 result 출력
* */

    public List<List<Integer>> combine(int n, int k){
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> arr = new ArrayList<>();
        dfs(result, arr, 1, n , k);
        return result;
    }

    private void dfs(List<List<Integer>> result, List<Integer> current, int start, int n, int k) {
        // 현재 조합의 길이가 k와 같다면 결과에 추가하고 반환합니다.
        if (current.size() == k) {
            result.add(new ArrayList<>(current));
            return;
        }

        // start부터 n까지의 숫자에 대해 반복.
        // n이 5라면 1~5를 for문 돌림
        for (int i = start; i <= n; i++) {
            // 현재 숫자를 조합에 추가.
            current.add(i);
            // 다음 요소를 선택하기 위해 재귀적으로 DFS를 호출.
            dfs(result, current, i + 1, n, k);
            // 백트래킹: 조합에서 마지막 숫자를 제거.
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Combinations cb = new Combinations();
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        List<List<Integer>> result = cb.combine(n, k);
        // 결과 출력
        System.out.println(result);
    }
}
