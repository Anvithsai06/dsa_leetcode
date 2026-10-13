"""class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        c=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n+1):
                res=nums[j]
                if res.count(target)>(j-i)//2:
                    c+=1
        return c"""
from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        c = 0
        n = len(nums)
        
        for i in range(n):
            t = 0
            for j in range(i, n):
                if nums[j] == target:
                    t += 1
                
                l = j - i + 1
                if t > l // 2:
                    c += 1
                    
        return c
