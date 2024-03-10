package codingTestStudy.week7;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class IPv6 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String[] split = input.split(":");
        StringBuilder stringBuilder = new StringBuilder();
        for (String s : split){
            if (s.isEmpty()){
                if (stringBuilder.length()==0) {
                    int length = 8 - split.length + 1;
                    for (int i = 0; i < length; i++) {
                        stringBuilder.append("0000:");
                    }
                }else {
                    stringBuilder.append("0000:");
                }
            }else {
                int length = 4-s.length();
                for (int i=0; i<length; i++){
                    stringBuilder.append("0");
                }
                stringBuilder.append(s).append(":");
            }
        }
        System.out.println(stringBuilder.substring(0, stringBuilder.length()-1));
    }
}
