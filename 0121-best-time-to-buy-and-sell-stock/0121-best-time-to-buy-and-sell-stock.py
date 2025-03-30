class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = 0
        # r = 0
        # prof = 0

        # for l in range(len(prices)):
        #     r=l
        #     while r <= len(prices)-1:
        #         if prof<prices[r]-prices[l]:
        #             prof = prices[r]-prices[l]
        #         r+=1
        # return prof

        l = 0
        profit = 0
        minprice = float('inf')

        for r in range(len(prices)):
            if prices[r] < minprice:
                minprice = prices[r]
                # print(minprice)
                l=r
            if prices[r]-prices[l] > profit:
                profit = prices[r]-prices[l]
                # print(profit)
        
        return profit 
            
