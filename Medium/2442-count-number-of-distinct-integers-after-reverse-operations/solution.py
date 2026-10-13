class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            n=str(i)
            a.append(int(n[::-1]))
        nums+=a
        return len(set(nums))
