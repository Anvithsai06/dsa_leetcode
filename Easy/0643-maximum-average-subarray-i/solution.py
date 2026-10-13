class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=0
        m=min(nums)-1
        s=0
        while r<len(nums):
            s+=nums[r]
            if r-l+1==k:
                m=max(s/k,m)
                s-=nums[l]
                l+=1
            r+=1
        return m
