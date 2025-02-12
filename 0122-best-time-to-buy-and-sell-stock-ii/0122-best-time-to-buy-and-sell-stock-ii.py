class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit[0] = 0
        # maxi = 0
        # for i in range(len(prices)):
        #     for j in range(len(prices)):
        #         if maxi < prices[j]-prices[i]:
        #             maxi = prices[j]-prices[i]
        

        # profit[i] = max(profit[i-1],profit[i-1]-buy[i]+sell[j])
                
        # for day i,
        # profit[i] = profit[i-1]
        # profit[i-1]-buy[i]+sell[j]

        # min_price = math.inf
        max_profit = 0
        for i in range(1,len(prices)):
            # if prices[i] < min_price:
            #     min_price = prices[i]
            if prices[i] > prices[i-1]:      
                max_profit += prices[i]-prices[i-1]

        return max_profit

