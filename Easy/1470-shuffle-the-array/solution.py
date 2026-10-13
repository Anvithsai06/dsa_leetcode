class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = nums[:n]
        second = nums[n:]
        final=[]
        for i in range(n):
            final.append(first[i])
            final.append(second[i])
        return final
