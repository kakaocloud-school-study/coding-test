package codingTestStudy.week4.Trie;

import java.util.ArrayList;
import java.util.List;

public class PalindromePairs {
    public boolean isPalindrome(String s){
        String s1 = s.toLowerCase();
        String s2 = new StringBuilder(s1).reverse().toString();
        return s1.equals(s2);
    }
    public List<List<Integer>> palindromePairs(String[] words) {
        List<Integer> result;
        List<List<Integer>> resultList = new ArrayList<>();
        for (int i=0; i<words.length; i++){
            for (int j=0; j<words.length; j++){
                if(i!=j){
                    if(isPalindrome(words[i]+words[j])){
                        result = new ArrayList<>();
                        result.add(i);
                        result.add(j);
                        resultList.add(result);
                    }
                }
            }
        }
        return resultList;
    }
}
