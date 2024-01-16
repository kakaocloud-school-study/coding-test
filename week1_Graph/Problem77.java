class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<Integer> nList = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            nList.add(i);
        }

        return getCombine(nList, k);
    }

    private List<List<Integer>> getCombine(List<Integer> nList, int k) {
        List<List<Integer>> retList = new ArrayList<>();
        int ls = nList.size();
        if (ls == k) {
            retList.add(nList);
        } else if (k == 1) {
            for (int num : nList) {
                retList.add(Arrays.asList(num));
            }
        } else {
            int iter = ls - k + 1;
            List<Integer> newList;
            for (int i = 0; i < iter; i++) {

                List<List<Integer>> subListCombine = getCombine(nList.subList(i + 1, ls), k-1);

                for (List<Integer> list : subListCombine) {
                    newList = new ArrayList<>(list);
                    newList.add(0, nList.get(i));
                    retList.add(newList);
                }
            }
        }

        return retList;
    }
}