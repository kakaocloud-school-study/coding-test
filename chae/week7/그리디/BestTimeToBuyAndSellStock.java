package codingTestStudy.week7.그리디;

public class BestTimeToBuyAndSellStock {
    public int maxProfit(int[] prices) {
        int total =0;
        for(int i=0; i<prices.length-1; i++){
            if(prices[i]<prices[i+1]){
                total+=prices[i+1]-prices[i];
            }
        }
        return total;
    }

    public static void main(String[] args) {
        BestTimeToBuyAndSellStock bestTimeToBuyAndSellStock = new BestTimeToBuyAndSellStock();
        int[] prices = {7,1,5,3,6,4};
        System.out.println(bestTimeToBuyAndSellStock.maxProfit(prices));
    }
}
