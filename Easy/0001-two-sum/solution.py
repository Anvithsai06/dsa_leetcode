class Solution(object):
    self=0
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in seen:
                return i,seen[a]
            seen[nums[i]]=i
