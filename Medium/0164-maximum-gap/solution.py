class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_diff=0
        l=len(nums)
        if l==1:
            return 0
        else:
            for i in range(1,l):
                if nums[i]-nums[i-1]>max_diff:
                    max_diff=nums[i]-nums[i-1]
        return max_diff
