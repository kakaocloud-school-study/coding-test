package LeetCode.injeong;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Permutations {

    /*문제 해결 로직
     * 1. 결과를 저장할 리스트를 초기화한다.
     * 2. 백트래킹 함수를 정의한다.
     * 3. 백트래킹을 실행한다.
     * */

    public List<List<Integer>> permute(int[] nums) {
        //출력 형태 => [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1 ,2],[3,2,1]]
        // List<Integer> 형태로 있는 것들을 다시 [ ]에 감싸야해서 List<List<Integer>> 자료구조를 씀.
        List<List<Integer>> result = new ArrayList<>();
        // 백트래킹을 위한 경로 추적 리스트
        List<Integer> path = new ArrayList<>();
        // 백트래킹 함수 호출
        backtrack(nums, path, result);
        return result;
    }

    private void backtrack(int[] nums, List<Integer> path, List<List<Integer>> result) {
        // 현재 경로가 nums 길이와 동일하면 결과에 추가
        // nums 배열의 모든 요소가 path리스트에 포함됐는지 확인
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int num : nums) {
            // 현재 숫자가 이미 경로에 있는지 확인
            // 순열은 각 숫자가 유일해야되니까.
            // 조건 맞으면 다음 반복 루프로 즉시 진행.
            if (path.contains(num)) continue;

            // 경로에 숫자 추가
            path.add(num);
            // 다음 단계로 이동
            backtrack(nums, path, result);
            // 백트래킹: 이전 상태로 되돌리기
            // 마지막으로 추가된 숫자 제거

            path.remove(path.size() - 1);
        }
    }
    public static void main(String[] args) {
            Permutations pm = new Permutations();
            Scanner sn = new Scanner(System.in);
            //입력받은 문자열을 처리하기 위해 input에 임시로 담아줌.
            String input = sn.nextLine();
            //[ ] 대괄호 삭제함. , 기준으로 split함.
            input = input.replaceAll("\\[|\\]","").trim();
            String[] numbers = input.split(",");

            // [1,2,3] -> 대괄호 삭제, ','구분자로 나눔
            // 공백제거하고 다시 배열 자료구조에 넣어줌.
            int[] nums = new int[numbers.length];
            for (int i = 0; i < numbers.length; i++) {
                nums[i] = Integer.parseInt(numbers[i].trim());
            }

            List<List<Integer>> result = pm.permute(nums);
            // 결과 출력
            System.out.println(result);
    }
}
