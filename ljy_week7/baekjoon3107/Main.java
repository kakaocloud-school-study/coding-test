package ljy_week7.baekjoon3107;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine(); // 입력 스트링

        str = f1(str);

        String[] strArr = str.split(":");

        for (int i = 0; i < strArr.length; i++) {
            strArr[i] = f2(strArr[i]);
        }
        
        System.out.println(String.join(":", strArr));
    }

    // 생략된 0의 그룹을 추가
    private static String f1(String str) {
        // 예외 처리
        if (str.contains("::")) {
            // 그룹이 생략되어있을 때
            String[] strArr = str.split("::");
            // 이 규칙은 한번만 사용할 수 있으므로 스트링이 둘로 나누어진다.
            String str1 = strArr[0];
            String str2 = strArr.length == 1 ? "" : strArr[1];

            int str1Num = str1.split(":").length;
            int str2Num = str2.split(":").length;
            int groupNum = 8 - str1Num - str2Num;

            // ::이 양끝에 있는지 두 스트링의 길이로 확인하고 0000으로 치환한다.
            String retStr = str1.length() == 0 ? "0000" : str1;
            for (int i = 0; i < groupNum; i++) {
                retStr = retStr + ":0000";
            }
            retStr = str2.length() == 0 ? retStr + ":0000" : retStr + ":" + str2;

            return retStr;
        }
        return str;
    }

    // 생략된 0을 추가
    private static String f2(String str) {
        String retStr = str;
        for (int i = 0; i < 4 - str.length(); i++) {
            retStr = "0" + retStr;
        }
        return retStr;
    }
    
}