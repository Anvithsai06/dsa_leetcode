class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        num=0
        l=len(nums)
        arr=[0]*l
        for i in range(l):
            num+=nums[i]
            arr[i]=num
        return arr
