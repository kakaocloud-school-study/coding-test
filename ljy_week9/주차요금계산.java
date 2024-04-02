import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        // 누적 시간 
        Map<String, Integer> accum = new HashMap<>();
        // 들어온 시간
        Map<String, Integer> time = new HashMap<>();
        // 차 번호 리스트
        Set<String> carSet = new HashSet<>();
        
        for (String record : records) {
            String[] arr = record.split(" ");
            int h = Integer.parseInt(arr[0].split(":")[0]);
            int m = Integer.parseInt(arr[0].split(":")[1]);
            
            carSet.add(arr[1]);
            
            if (!time.containsKey(arr[1])) {
                time.put(arr[1], h * 60 + m);
            } else {
                int start = time.get(arr[1]);
                int end = h * 60 + m;
                
                accum.putIfAbsent(arr[1], 0);
                accum.put(arr[1], accum.get(arr[1]) + end - start);
                
                time.remove(arr[1]);
            }
        }
        
        String[] carNumArr = carSet.toArray(new String[0]);
        
        Arrays.sort(carNumArr);
        
        int[] answer = new int[carNumArr.length];
        
        for (int i = 0; i < answer.length; i++) {
            // OUT이 안되었을 때
            if ( time.containsKey(carNumArr[i])) {
                accum.putIfAbsent(carNumArr[i], 0);
                answer[i] = getTotal(accum.get(carNumArr[i]) 
                                     + 23 * 60 + 59 - time.get(carNumArr[i]), fees);
            }
            else {
                answer[i] = getTotal(accum.get(carNumArr[i]), fees);
            }
        }
        
        return answer;
    }
    
    private int getTotal(int t, int[] fees) {
        if (t <= fees[0]) return fees[1];
        else return fees[1] + (int) Math.ceil((double)(t - fees[0])/(double)fees[2]) * fees[3];
    }
}