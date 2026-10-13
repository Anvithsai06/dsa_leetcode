class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        su = nums[0]
        for i in range(0,len(nums)-1):
            if nums[i+1] == nums[i]+1:
                su += nums[i]+1
            else:
                break
        while su in nums:
            su += 1
        return su
