package codingTestStudy.week7.그리디;

import java.util.Arrays;

public class AssignCookies {
    public int findContentChildren(int[] g, int[] s) {
        int count = 0;
        int a = 0;
        int b = 0;
        Arrays.sort(g);
        Arrays.sort(s);
        while (a <g.length && b <s.length){
            if (g[a]<=s[b]){
                count++;
                a++;
                b++;
            }else{
                b++;
            }
        }
        return count;
    }
}
