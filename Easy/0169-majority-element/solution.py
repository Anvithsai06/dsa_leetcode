class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr=set(nums)
        maj=0
        for i in arr:
            if nums.count(i)>=len(nums)/2:
                maj=i
        return maj
