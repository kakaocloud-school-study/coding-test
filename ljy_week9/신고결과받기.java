import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        
        // 중복 제거
        String[] report2 = new HashSet<String>(Arrays.asList(report)).toArray(new String[0]);
        
        // 신고된 횟수 저장
        Map<String, List<String>> map = new HashMap<>();
        
        for (String rep : report2) {
            String[] sep = rep.split(" ");
            
            map.putIfAbsent(sep[1], new ArrayList<>());
            map.get(sep[1]).add(sep[0]);
        }
        
        // 순회하면서 횟수 세고 answer에 더함
        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            if (entry.getValue().size() >= k) {
                for (String name : entry.getValue()) {
                    answer[Arrays.asList(id_list).indexOf(name)]++;
                }
            }
        }
        return answer;
    }
}