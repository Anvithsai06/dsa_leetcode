class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        s=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    s.append(prices[i]-prices[j])
                    break
            if len(s)!=i+1:
                s.append(prices[i])
        return s
