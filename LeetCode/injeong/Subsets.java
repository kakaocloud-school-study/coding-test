package LeetCode.injeong;

import java.util.*;

public class Subsets {
    /*문제풀이로직
    *1. 결과담을 리스트 초기화 ( 여기서 dfs 첫 호출 이뤄짐 )
    *2. dfs 함수 정의
    *3. dfs 함수 호출
    *4. main에서 result 출력
    * */

    public List<List<Integer>> subset (int[] nums){
        //결과 초기화
        List<List<Integer>> result = new ArrayList<>();
        //path 초기화
        List<Integer> path = new ArrayList<>();
        //dfs 함수 초기호출
        dfs(result, nums, path, 0);
        return result;
    }

    private void dfs(List<List<Integer>> result, int[]nums, List<Integer>path, int start){
        //조건 상관없이 result에 넣음.
        result.add(new ArrayList<>(path)); // 처음엔 path가 null이니까 null값 들어감.

        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]); // start 부터 path에 담아줌.
            dfs(result, nums, path, start+1);
            path.remove(path.size()-1); // 백트래킹
        }
    }

    public static void main(String[] args) {
        Subsets ss = new Subsets();
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        input = input.replaceAll("\\[|\\]","").trim();
        String[] numbers = input.split(",");

        int[] nums = new int[numbers.length];
        for(int i = 0; i < numbers.length; i++){
            nums[i] = Integer.parseInt(numbers[i].trim());
        }

        List<List<Integer>> result = ss.subset(nums);
        System.out.println(result);
    }
}
