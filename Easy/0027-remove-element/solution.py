class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        for i in nums[:]:
            if i == val:
                nums.remove(val)
            c+=1
        return c
