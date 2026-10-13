class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        miss=[]
        mn = nums[0]
        mx = nums[-1]
        ln = len(nums)
        for i in range(mn,mx+1):
            if i not in nums:
                miss.append(i)
        return miss
