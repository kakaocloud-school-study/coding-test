package codingTestStudy.week1;

import java.util.ArrayList;
import java.util.List;

public class Permutations {
    static List<List<Integer>> result;
    static List<Integer> array;
    public static List<List<Integer>> permute(int[] nums) {
        boolean[] visited = new boolean[nums.length];
        int[] output = new int[nums.length];
        result = new ArrayList<>();
        array = new ArrayList<>();
        for (int i=0; i< nums.length; i++){
            array.add(i);
        }
        bfs(nums, visited, output, 0);
        return result;
    }


    public static void bfs(int[] nums, boolean[] visited, int[] output ,int index){
        if(index == nums.length){
            result.add(new ArrayList<>(array));
            return;
        }

        for (int j = 0; j < nums.length; j++) {
            if (!visited[j]) {
                visited[j] = true;
                array.set(index, nums[j]);
                bfs(nums, visited,output,index+1);
                visited[j] = false;
            }
        }
    }
}
