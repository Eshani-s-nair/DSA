//Problem : 121. Best Time to Buy and Sell Stock
//Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

//Brute Force Approach
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                profit = Math.max(profit, prices[j] - prices[i]);
            }
        }
        return profit;
    }
}
//Time Complexity : O(n^2)

//optimized Approach
class Solution {
    public int maxProfit(int[] prices) {
        int profit=0;
        int smaller=Integer.MAX_VALUE;
        for (int i =0;i<prices.length;i++){
           if(prices[i]<smaller){
            smaller=prices[i];
           }
           else if((prices[i]-smaller)>profit){
            profit=prices[i]-smaller;
           }
        }
       return profit; 
}
}
