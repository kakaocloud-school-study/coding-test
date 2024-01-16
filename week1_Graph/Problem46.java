class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> numList = new ArrayList<>();
        for (int num : nums) {
            numList.add(num);
        }

        return getPermute(numList);
    }

    private List<List<Integer>> getPermute(List<Integer> numList) {
        List<List<Integer>> retList = new ArrayList<>();

        if (numList.size() == 1) {
            retList.add(numList);
        } else if (numList.size() == 2) {
            List<Integer> numList2 = new ArrayList<>();
            numList2.add(numList.get(1));
            numList2.add(numList.get(0));

            retList.add(numList);
            retList.add(numList2);
        } else {
            for (int i = 0; i < numList.size(); i++) {
                int selectedNum = numList.get(i);
                List<Integer> subList = new ArrayList<>(numList);
                subList.remove(i);

                List<List<Integer>> subListPermute = getPermute(subList);

                for (List<Integer> list : subListPermute) {
                    list.add(0, selectedNum);
                    retList.add(list);
                }
            }
        }

        return retList;
    }
}