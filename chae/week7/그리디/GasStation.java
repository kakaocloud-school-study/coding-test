package codingTestStudy.week7.그리디;

public class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0;
        int now = 0;
        int start = 0;
        for (int i=0; i<gas.length; i++){
            total += gas[i]-cost[i];
            now += gas[i]-cost[i];
            if (now <0){
                start = i+1;
                now = 0;
            }
        }
        return total>=0?start:-1;
    }
}
