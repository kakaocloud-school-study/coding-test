class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> argList = new ArrayList<>();

        for (char c : digits.toCharArray()) {
            argList.add("" + c);
        }
        return digitsToString(argList);
    }

    private List<String> digitsToString(List<String> digitArr) {
        List<String> retList = new ArrayList<>();
        if (digitArr.size() == 0) {
            return retList;
        }
        if (digitArr.size() == 1) {
            int num = Integer.parseInt(digitArr.get(0));
            switch (num) {
                case 2:
                    retList = new ArrayList<String>(Arrays.asList("a", "b", "c"));
                    break;
                case 3:
                    retList = new ArrayList<String>(Arrays.asList("d", "e", "f"));
                    break;
                case 4:
                    retList = new ArrayList<String>(Arrays.asList("g", "h", "i"));
                    break;
                case 5:
                    retList = new ArrayList<String>(Arrays.asList("j", "k", "l"));
                    break;
                case 6:
                    retList = new ArrayList<String>(Arrays.asList("m", "n", "o"));
                    break;
                case 7:
                    retList = new ArrayList<String>(Arrays.asList("p", "q", "r", "s"));
                    break;
                case 8:
                    retList = new ArrayList<String>(Arrays.asList("t", "u", "v"));
                    break;
                case 9:
                    retList = new ArrayList<String>(Arrays.asList("w", "x", "y", "z"));
                    break;
            }
        } else {
            int l = digitArr.size();
            List<String> stringList = digitsToString(digitArr.subList(0, l - 1));
            List<String> charString = digitsToString(digitArr.subList(l-1, l));
            for (String str : stringList) {
                for (String cstr : charString) {
                    retList.add(str+cstr);
                }
            }
        }
        return retList;
    }
}