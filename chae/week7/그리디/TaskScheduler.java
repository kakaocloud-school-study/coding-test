package codingTestStudy.week7.그리디;

public class TaskScheduler {
    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for (char c : tasks){
            count[c-'A']++;
        }
        int max = 0;
        for (int i=0; i<26; i++){
            if (max<count[i]){
                max = count[i];
            }
        }
        int maxCount = 0;
        for (int i=0; i<26; i++){
            if (max==count[i]){
                maxCount++;
            }
        }
        return Math.max(tasks.length, (max-1)*(n+1)+maxCount);
    }

    public static void main(String[] args) {
        TaskScheduler taskScheduler = new TaskScheduler();
        char[] tasks = {'A','A','A','B','B','B'};
        int n = 2;
        System.out.println(taskScheduler.leastInterval(tasks, n));
    }
}
