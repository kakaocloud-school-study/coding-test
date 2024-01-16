class Solution {


    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> numList = new ArrayList<>();

        for (int num : nums) {
            numList.add(num);
        }

        return getSubsets(numList);
    }

    private List<List<Integer>> getSubsets(List<Integer> numList) {
        List<List<Integer>> retList = new ArrayList<>();

        if (numList.size() == 1) {
            retList.add(new ArrayList<>());
            retList.add(numList);
        } else {
            List<List<Integer>> subsets = getSubsets(numList.subList(0, numList.size() - 1));
            int num = numList.get(numList.size() - 1);
            for (List<Integer> subset : subsets) {
                retList.add(subset);
                List<Integer> newSubset = new ArrayList<>(subset);
                newSubset.add(num);
                retList.add(newSubset);
            }
        }

        return retList;
    }
}