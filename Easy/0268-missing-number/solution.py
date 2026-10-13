class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=min(nums)
        h=max(nums)
        for i in range(l,h):
            if i not in nums:
                return i
        return h+1 if 0 in nums else 0
