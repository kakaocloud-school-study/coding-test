package codingTestStudy.week5.sort;

import java.util.Arrays;
import java.util.Objects;

public class ValidAnagram1 {
    public static boolean isAnagram(String s, String t) {
        String[] array1 = s.split("");
        String result1 = Arrays.toString(Arrays.stream(array1).sorted().toArray());

        String[] array2 = t.split("");
        String result2= Arrays.toString(Arrays.stream(array2).sorted().toArray());
        System.out.println(result1 +"          "+ result2);
        return Objects.equals(result1, result2);
    }

    public static void main(String[] args) {
        String s = "anagram";
        String t ="nagaram";
        isAnagram(s, t);
    }
}
