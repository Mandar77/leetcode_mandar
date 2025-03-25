int maxProfit(int* prices, int pricesSize) {
    if (pricesSize == 0) return 0;

    int minPrice = prices[0];  // Track the minimum price
    int maxProfit = 0;         // Track the maximum profit

    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] < minPrice) {
            minPrice = prices[i];  // Update minimum price
        } else {
            int profit = prices[i] - minPrice;  // Calculate profit
            if (profit > maxProfit) {
                maxProfit = profit;  // Update max profit
            }
        }
    }
    return maxProfit;
}