class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        r=0
        i=1
        while True:
            r=k*i
            i+=1
            if r not in nums:
                return r
