class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''c=0
        for i in nums:
            if i == 0:
                nums.remove(i)
                c+=1
        l=[0]*c
        nums=nums.append(l)'''
        res=[]
        for i in nums:
            if i!=0:
                res.append(i)
        l=[0]*(len(nums)-len(res))
        res=res+l
        for i in range(len(nums)):
            nums[i]=res[i]
