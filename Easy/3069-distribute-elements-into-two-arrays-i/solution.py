class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[nums[0]]
        nums.pop(0)
        arr2=[nums[0]]
        nums.pop(0)
        while(nums):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[0])
                nums.pop(0)
            else:
                arr2.append(nums[0])
                nums.pop(0)
        return arr1+arr2
