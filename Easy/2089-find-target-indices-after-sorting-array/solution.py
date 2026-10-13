class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        s_l,t=sorted(nums),len(nums)
        l=[]
        for i in range(t):
            if s_l[i] == target:
                l.append(i)
        return l
