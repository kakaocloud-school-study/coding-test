package codingTestStudy.week6.bit;


public class HammingDistance2 {
    public int hammingDistance(int x, int y) {
        char[] result = Integer.toBinaryString(x^y).toCharArray();
        int count =0;
        for (Character c : result){
            if (c=='1'){
                count++;
            }
        }
        return count;
    }
}
