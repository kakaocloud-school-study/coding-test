// 교재 풀이
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        List<int[]> merged = new ArrayList<>();

        for (int[] i : intervals) {
            if (!merged.isEmpty() && i[0] <= merged.get(merged.size() - 1)[1]) {
                merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], i[1]);
            } else{
                merged.add(i);
            }
        }

        return merged.toArray(new int[merged.size()][2]);
    }
}