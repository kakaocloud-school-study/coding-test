package LeetCode.injeong;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PhoneNumber{

    //다이얼 각 숫자에 해당하는 문자를 인덱스로 접근하도록 배열 생성.
    private static final String[] PHONE_NUMBER = {
            "",     // 0번은 빈 문자열
            "",     // 1번도 빈 문자열
            "abc",  // 2번
            "def",  // 3번
            "ghi",  // 4번
            "jkl",  // 5번
            "mno",  // 6번
            "pqrs", // 7번
            "tuv",  // 8번
            "wxyz"  // 9번
    };

    // 주어진 숫자 조합으로 만들 수 있는 모든 문자 조합을 반환하는 메소드
    public List<String> letterCombinations(String digits) {
        List<String> results = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return results;
        }
        //문자 조합을 동적으로 구성하고 변경하기 위해 StringBuilder 객체 생성
        StringBuilder current = new StringBuilder();
        backtrack(results, current, digits, 0);
        return results;
    }

    // 백트래킹을 수행하는 메소드
    private void backtrack(List<String> results, StringBuilder current, String digits, int index) {
        if (index == digits.length()) {//모든 숫자를 처리했다면 현재 조합을 결과에 추가하고 리턴
            results.add(current.toString());
            return;
        }

        //digits.charAt(index)는 String이다.
        //문자 String은 아스키코드 값으로 저장된다.
        //'2'-'0'은 50-48과 같으며 결과는 2다. 이렇게 정수형 숫자를 얻을 수 있다.
        String letters = PHONE_NUMBER[digits.charAt(index) - '0'];
        for (char letter : letters.toCharArray()) {//toCharArray()로 문자열을 문자배열로 변환함.
            //char letter는 배열의 각 원소, 즉 개별 문자를 나타낸다.
            current.append(letter); // 현재 문자 추가
            backtrack(results, current, digits, index + 1); // 다음 문자로 재귀 호출
            current.deleteCharAt(current.length() - 1); // 백트래킹: 마지막 문자 제거
        }
    }

    public static void main(String[] args) {
        //간단한 문자열을 다루니 scanner사용함
        Scanner scanner = new Scanner(System.in);
        String digits = scanner.nextLine();


        PhoneNumber pn = new PhoneNumber();
        //문자열들의 조합을 순서상관없는 배열로 출력할 것이기 때문에
        //List<String> 씀.
        List<String> combinations = pn.letterCombinations(digits);
        System.out.println(combinations);
    }
}
