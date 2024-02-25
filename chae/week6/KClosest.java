package codingTestStudy.week6;

public class KClosest {
    public int[][] kClosest(int[][] points, int k) {
        int length = points.length;
        int[] total = new int[length];
        boolean[] visited = new boolean[length];
        int[][] result = new int[k][2];
        for (int i=0; i<length;i++){
            total[i] = (int) (Math.pow(points[i][0],2)+Math.pow(points[i][1],2));
        }
        int count=0;
        int minIndex = 0;
        while (count<k) {
            int min = Integer.MAX_VALUE;
            for (int j = 0; j < length; j++) {
                if (min > total[j]&& !visited[j]) {
                    min = total[j];
                    minIndex = j;
                }
            }
            visited[minIndex] = true;
            result[count] = points[minIndex];
            count++;
        }
        return result;
    }
}
