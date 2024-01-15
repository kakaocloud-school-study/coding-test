package LeetCode.injeong;
import javax.imageio.stream.ImageInputStream;
import java.util.*;
public class CombinationSum {
    /*문제풀이로직
    * 1.결과를 저장할 리스트를 초기화해준다.
    * 2. dfs함수 정의 (가능한 모든 조합을 탐색, 각 단계에서 선택한 숫자의 합이 target이면 result에 add)
    * 3. dfs실행
    * 4. main 함수에서 결과반환
    * */
    public List<List<Integer>> comSum (int[] candi, int target){
        //결과 초기화
        List<List<Integer>> result = new ArrayList<>();
        //ArrayDeque는 앞에서도 뒤에서도 요소를 추가, 제거 가능하다.
        Deque<Integer> path = new ArrayDeque<>();
        //dfs실행
        dfs(candi, target, 0, 0, path, result);
        return result;
    }


    private void dfs(int[] candi, int target, int start, int sum, Deque<Integer> path, List<List<Integer>> result){
        if(sum == target){
            result.add(new ArrayList<>(path)); //result.add(path)로 하면 데이터의 주소를 저장하게됨.
            //path의 참조가 가리키는 내용은 계속 변화하기 때문에 (재귀함수 호출)
            //참조 주소를 가리키면 최종적으로 모든 조합이 마지막 상태의 path와 동일해지게됨.
            // 그래서 새로운 리스트를 path를 복사해서 생성해줘야함. (path변경에 독립적으로 되도록)
        }
        if (sum > target){
            return;
        }

        //candi 숫자 집합의 길이만큼 반복함.
        for(int i = start; i < candi.length; i++) {
            path.addLast(candi[i]);
            //처음에 결과를 초기화하고 dfs함수를 호출하는 부분에서 start를 0으로 부를거임. 그럼 제시된 candi의 첫번째 인덱스부터 path에 추가됨.
            dfs(candi, target, i, sum + candi[i], path, result);
            //sum도 첫 호출에서 0을 부름. candi[start]를 하나씨 누적하며 dfs를 부르는 것.
            //candi.length만큼 dfs돌린다음에 처음 for문의 다음 루프로 간다.
            //순열과 조합에서는 start에 +1을 해줘서 숫자 중복이 없었지만, 조합의 합에서는 숫자 중복을 허용한다.
            path.removeLast(); //백트래킹: 마지막 요소를 제거한다.
        }
    }

    public static void main(String[] args) {
        CombinationSum cs = new CombinationSum();
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        int target = sc.nextInt();
        //[ ] 대괄호 삭제함. , 기준으로 split함.
        input = input.replaceAll("\\[|\\]","").trim();
        String[] numbers = input.split(",");

        // 대괄호 삭제, ','구분자로 나눔
        // 공백제거하고 다시 배열 자료구조에 넣어줌.
        int[] nums = new int[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            nums[i] = Integer.parseInt(numbers[i].trim());
        }

        List<List<Integer>> result = cs.comSum(nums, target);
        System.out.println(result);

    }
}
