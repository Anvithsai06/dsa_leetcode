class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        pg=[]
        for i in range(len(stones)):
            heapq.heappush(pg,-stones[i])
        while len(pg)>1:
            val1=-heapq.heappop(pg)
            val2=-heapq.heappop(pg)
            if val1 != val2:
                heapq.heappush(pg,-abs(val1-val2))
        return -pg[0] if pg else 0
