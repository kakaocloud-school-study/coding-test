class Solution {
    List<List<Integer>> retList = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> candList = new ArrayList<>();
        for (int c : candidates) {
            candList.add(c);
        }

        search(candList, target, new ArrayList<>());

        return retList;
    }

    private void search(List<Integer> candList, int target, List<Integer> curList) {
        for (int i = 0; i < candList.size(); i++) {
            int cand = candList.get(i);
            curList.add(cand);
            if (cand == target) {
                retList.add(new ArrayList<>(curList));
            } else if (cand < target) {
                search(candList.subList(i, candList.size()), target - cand, curList);
            }
            curList.remove(curList.size() - 1);
        }
    }
}